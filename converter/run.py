"""
Example showing how to run Scrapy and Uvicorn in the same process.

This is probably not a good idea :-) but here's how if you need it.

Usage:

    $ . .venv/bin/activate
    $ python -m converter.run

Then the Swagger UI will be at http://127.0.0.1:8000/docs .

This works by making both Uvicorn and Scrapy use asyncio as their backend.
Scrapy is based on Twisted. We use the twisted asyncioreactor. When that
is running, we start the uvicorn server. Then when we get the POST request,
we can just launch Scapy via CrawlerRunner (not CrawlerProcess).

Note that you cannot call this script via something like

    uvicorn --factory converter.run:create_app

since we need to start the reactor before the uvicorn server.
"""


import os
from scrapy.cmdline import execute

import uvicorn
import fastapi as fapi
import fastapi.middleware.cors as fapicors
import pydantic as pd
import scrapy.crawler as cw
import scrapy.utils.project as sproj
from converter.spiders.generic_spider import GenericSpider
from scrapy import signals
from scrapy.signalmanager import dispatcher
from scrapy.utils.defer import deferred_to_future, deferred_from_coro
from scrapy.utils.serialize import ScrapyJSONEncoder



def run():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    execute(
        [
            "scrapy",
            "crawl",
            "-a",
            "cleanrun=true",
            "-o",
            "out/items.json",
            "wirlernenonline_spider",
        ]
    )


class Data(pd.BaseModel):
    url: str

class Result(pd.BaseModel):
    resultjson: str = ""


def create_app() -> fapi.FastAPI:

    app = fapi.FastAPI()

    origins = ['*']

    app.add_middleware(
        fapicors.CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/_ping")
    def _ping():
        pass


    @app.post("/metadata")
    async def metadata(data: Data) -> Result:
        print("TARGET_URL", data.url)

        project_settings = sproj.get_project_settings()
        results = []
        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        url = 'https://de.wikipedia.org/wiki/G%C3%B6ttingen'
        c = cw.CrawlerRunner(project_settings)
        # Convert the 'deferred' to something we can 'await':
        await deferred_to_future(c.crawl(GenericSpider, url=url))

        lom = results[0]['lom']
        encoder = ScrapyJSONEncoder()
        resultjson = encoder.encode(lom)

        return Result(
            # why do we put this as a json encoded string into the response, and not directly as json?
            resultjson=resultjson,
        )

    return app


def start_ws_service(*args):
    config = uvicorn.Config("converter.run:create_app", port=8000, log_level="info", loop="asyncio", factory=True)
    server = uvicorn.Server(config)
    print("calling serve")
    
    from twisted.internet import reactor
    d = deferred_from_coro(server.serve())
    # shutdown Twisted reactor (and the whole process) when the web server shuts down
    d.addBoth(lambda *args: reactor.stop())


if __name__ == "__main__":
    from twisted.internet import asyncioreactor
    asyncioreactor.install()

    from twisted.internet import reactor
    reactor.callWhenRunning(start_ws_service)
    reactor.run()
