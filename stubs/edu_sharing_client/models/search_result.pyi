from typing import Any, Optional

class SearchResult:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, nodes: Optional[Any] = ..., pagination: Optional[Any] = ..., facettes: Optional[Any] = ..., ignored: Optional[Any] = ...) -> None: ...
    @property
    def nodes(self): ...
    @nodes.setter
    def nodes(self, nodes: Any) -> None: ...
    @property
    def pagination(self): ...
    @pagination.setter
    def pagination(self, pagination: Any) -> None: ...
    @property
    def facettes(self): ...
    @facettes.setter
    def facettes(self, facettes: Any) -> None: ...
    @property
    def ignored(self): ...
    @ignored.setter
    def ignored(self, ignored: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
