from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import Request as Request
from typing import Any

logger: Any

class UrlLengthMiddleware:
    maxlength: Any = ...
    def __init__(self, maxlength: Any) -> None: ...
    @classmethod
    def from_settings(cls, settings: Any): ...
    def process_spider_output(self, response: Any, result: Any, spider: Any): ...
