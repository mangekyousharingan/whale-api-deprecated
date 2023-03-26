from abc import ABC, abstractmethod

from core.models.responses import AddressWealthResponse


class DataPort(ABC):
    @abstractmethod
    async def get_address_wealth(self, address: str) -> AddressWealthResponse:
        pass

    @abstractmethod
    async def get_address_transactions(self, address: str) -> list[dict]:
        pass
