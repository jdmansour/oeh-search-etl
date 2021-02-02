from typing import Any, Optional

class StatisticsGlobal:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, overall: Optional[Any] = ..., groups: Optional[Any] = ..., user: Optional[Any] = ...) -> None: ...
    @property
    def overall(self): ...
    @overall.setter
    def overall(self, overall: Any) -> None: ...
    @property
    def groups(self): ...
    @groups.setter
    def groups(self, groups: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
