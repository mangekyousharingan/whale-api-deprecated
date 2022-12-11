from dataclasses import dataclass
from typing import Callable

from src.core.models.requests import AddressWealthRequest
from src.core.models.responses import AddressWealthResponse
from src.core.ports.DataPort import DataPort


@dataclass
class AddressWealth:
    adapter_factory: Callable[[str], DataPort]

    async def __call__(self, request: AddressWealthRequest) -> AddressWealthResponse:
        adapter = self.adapter_factory(request.coin)
        response = await adapter.get_address_wealth(request.address)
        response.coin = request.coin
        return response