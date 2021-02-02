from typing import Any, Optional

class DynamicConfig:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, node_id: Optional[Any] = ..., value: Optional[Any] = ...) -> None: ...
    @property
    def node_id(self): ...
    @node_id.setter
    def node_id(self, node_id: Any) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
