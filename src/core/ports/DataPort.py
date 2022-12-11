from abc import ABC, abstractmethod

from src.core.models.responses import AddressWealthResponse


class DataPort(ABC):
    @abstractmethod
    async def get_address_wealth(self, address: str) -> AddressWealthResponse:
        pass