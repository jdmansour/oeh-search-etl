from typing import Any, Optional

class SearchParameters:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, criterias: Optional[Any] = ..., facettes: Optional[Any] = ...) -> None: ...
    @property
    def criterias(self): ...
    @criterias.setter
    def criterias(self, criterias: Any) -> None: ...
    @property
    def facettes(self): ...
    @facettes.setter
    def facettes(self, facettes: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
