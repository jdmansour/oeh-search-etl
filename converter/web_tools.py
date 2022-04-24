import asyncio
import json
from enum import Enum

import html2text
import pyppeteer
import requests
from playwright.async_api import async_playwright
from scrapy.utils.project import get_project_settings

from converter import env


class WebEngine(Enum):
    # Splash (default engine)
    Splash = 'splash',
    # Pyppeteer is controlling a headless Chrome browser
    Pyppeteer = 'pyppeteer'
    # Playwright is controlling a headless Chrome browser
    Playwright = 'playwright'


class WebTools:
    @staticmethod
    def getUrlData(url: str, engine=WebEngine.Splash):
        if engine == WebEngine.Splash:
            return WebTools.__getUrlDataSplash(url)
        elif engine == WebEngine.Pyppeteer:
            return WebTools.__getUrlDataPyppeteer(url)
        elif engine == WebEngine.Playwright:
            return WebTools.__getUrlDataPlaywright(url)

        raise Exception("Invalid engine")

    @staticmethod
    def __getUrlDataPyppeteer(url: str):
        # html = "test"
        html = asyncio.run(WebTools.fetchDataPyppeteer(url))
        return {"html": html, "text": WebTools.html2Text(html), "cookies": None, "har": None}

    @staticmethod
    def __getUrlDataPlaywright(url: str):
        html = asyncio.run(WebTools.fetchDataPlaywright(url))
        return {"html": html, "text": WebTools.html2Text(html), "cookies": None, "har": None}

    @staticmethod
    def __getUrlDataSplash(url: str):
        settings = get_project_settings()
        # html = None
        if settings.get("SPLASH_URL"):
            result = requests.post(
                settings.get("SPLASH_URL") + "/render.json",
                json={
                    "html": 1,
                    "iframes": 1,
                    "url": url,
                    "wait": settings.get("SPLASH_WAIT"),
                    "headers": settings.get("SPLASH_HEADERS"),
                    "script": 1,
                    "har": 1,
                    "response_body": 1,
                },
            )
            data = result.content.decode("UTF-8")
            j = json.loads(data)
            html = j['html'] if 'html' in j else ''
            text = html
            text += '\n'.join(list(map(lambda x: x["html"], j["childFrames"]))) if 'childFrames' in j else ''
            cookies = result.cookies.get_dict()
            return {"html": html,
                    "text": WebTools.html2Text(text),
                    "cookies": cookies,
                    "har": json.dumps(j["har"])}
        else:
            return {"html": None, "text": None, "cookies": None, "har": None}

    @staticmethod
    async def fetchDataPyppeteer(url: str):
        browser = await pyppeteer.connect({
            'browserWSEndpoint': env.get('PYPPETEER_WS_ENDPOINT'),
            'logLevel': 'WARN'
        })
        page = await browser.newPage()
        await page.goto(url)
        content = await page.content()
        # await page.close()
        return content

    @staticmethod
    async def fetchDataPlaywright(url: str):
        # relevant docs for this implementation: https://hub.docker.com/r/browserless/chrome#playwright and
        # https://playwright.dev/python/docs/api/class-browsertype#browser-type-connect-over-cdp
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp(endpoint_url=env.get("PLAYWRIGHT_WS_ENDPOINT"))
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle", timeout=90000)
            # waits for page to fully load (= no network traffic for 500ms),
            # maximum timeout: 90s
            content = await page.content()
            # await page.close()
            return content

    @staticmethod
    def html2Text(html: str):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        return h.handle(html)
