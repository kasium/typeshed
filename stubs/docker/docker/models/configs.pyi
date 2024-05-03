from collections.abc import Sequence

from .resource import Collection, Model

class Config(Model):
    id_attribute: str
    @property
    def name(self) -> str: ...
    def remove(self) -> bool: ...

class ConfigCollection(Collection[Config]):
    model: type[Config]
    def create(self, **kwargs) -> Config: ...  # type:ignore[override]
    def get(self, config_id: str) -> Config: ...
    def list(self, **kwargs) -> Sequence[Config]: ...
