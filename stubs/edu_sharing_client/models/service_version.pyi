from typing import Any, Optional

class ServiceVersion:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, repository: Optional[Any] = ..., renderservice: Optional[Any] = ..., major: Optional[Any] = ..., minor: Optional[Any] = ...) -> None: ...
    @property
    def repository(self): ...
    @repository.setter
    def repository(self, repository: Any) -> None: ...
    @property
    def renderservice(self): ...
    @renderservice.setter
    def renderservice(self, renderservice: Any) -> None: ...
    @property
    def major(self): ...
    @major.setter
    def major(self, major: Any) -> None: ...
    @property
    def minor(self): ...
    @minor.setter
    def minor(self, minor: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
