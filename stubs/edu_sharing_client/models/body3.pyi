from typing import Any, Optional

class Body3:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, xml: Optional[Any] = ...) -> None: ...
    @property
    def xml(self): ...
    @xml.setter
    def xml(self, xml: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
