from typing import Any, Optional

class MdsType:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, type: Optional[Any] = ..., properties: Optional[Any] = ...) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    @property
    def properties(self): ...
    @properties.setter
    def properties(self, properties: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
