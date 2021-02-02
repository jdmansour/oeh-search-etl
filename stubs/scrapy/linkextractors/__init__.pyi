from scrapy.utils.deprecate import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.utils.misc import arg_to_iter as arg_to_iter
from scrapy.utils.url import url_has_any_extension as url_has_any_extension, url_is_from_any_domain as url_is_from_any_domain
from typing import Any

IGNORED_EXTENSIONS: Any

class FilteringLinkExtractor:
    def __new__(cls, *args: Any, **kwargs: Any): ...
    link_extractor: Any = ...
    allow_res: Any = ...
    deny_res: Any = ...
    allow_domains: Any = ...
    deny_domains: Any = ...
    restrict_xpaths: Any = ...
    canonicalize: Any = ...
    deny_extensions: Any = ...
    restrict_text: Any = ...
    def __init__(self, link_extractor: Any, allow: Any, deny: Any, allow_domains: Any, deny_domains: Any, restrict_xpaths: Any, canonicalize: Any, deny_extensions: Any, restrict_css: Any, restrict_text: Any) -> None: ...
    def matches(self, url: Any): ...
