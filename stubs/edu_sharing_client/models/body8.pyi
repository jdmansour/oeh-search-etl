from typing import Any, Optional

class Body8:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, mediacenters: Optional[Any] = ...) -> None: ...
    @property
    def mediacenters(self): ...
    @mediacenters.setter
    def mediacenters(self, mediacenters: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
