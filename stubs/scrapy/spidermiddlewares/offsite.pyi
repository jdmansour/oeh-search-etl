from scrapy import signals as signals
from scrapy.http import Request as Request
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from typing import Any

logger: Any

class OffsiteMiddleware:
    stats: Any = ...
    def __init__(self, stats: Any) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Any): ...
    def process_spider_output(self, response: Any, result: Any, spider: Any) -> None: ...
    def should_follow(self, request: Any, spider: Any): ...
    def get_host_regex(self, spider: Any): ...
    host_regex: Any = ...
    domains_seen: Any = ...
    def spider_opened(self, spider: Any) -> None: ...

class URLWarning(Warning): ...
class PortWarning(Warning): ...
