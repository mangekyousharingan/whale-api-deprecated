from dataclasses import dataclass
from typing import Callable

from src.core.models.requests import AddressTxsBalanceRequest
from src.core.models.responses import AddressTxsBalanceResponse
from src.core.ports.DataPort import DataPort


@dataclass
class AddressTxBalance:
    adapter_factory: Callable[[str], DataPort]

    async def __call__(
        self, request: AddressTxsBalanceRequest
    ) -> AddressTxsBalanceResponse:
        adapter = self.adapter_factory(request.coin)
        response = await adapter.get_address_transactions(request.address)
        response.coin = request.coin
        response.address = request.address
        return response
