from typing import Any

class Create:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, only_metadata: bool = ...) -> None: ...
    @property
    def only_metadata(self): ...
    @only_metadata.setter
    def only_metadata(self, only_metadata: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
