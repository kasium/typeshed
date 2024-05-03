from collections.abc import Sequence
from typing import Any

from .resource import Collection, Model

class Volume(Model):
    id_attribute: str
    @property
    def name(self) -> str: ...
    def remove(self, force: bool = False) -> None: ...

class VolumeCollection(Collection[Volume]):
    model: type[Volume]
    def create(self, name: str | None = None, **kwargs) -> Volume: ...  # type:ignore[override]
    def get(self, volume_id: str) -> Volume: ...
    def list(self, **kwargs) -> Sequence[Volume]: ...
    def prune(self, filters: dict[str, Any] | None = None) -> dict[str, Any]: ...
