from dataclasses import dataclass
from typing import Callable

from src.core.models.requests import AddressTxsBalanceRequest
from src.core.models.responses import AddressTxsBalanceResponse
from src.core.ports.DataPort import DataPort


@dataclass
class AddressWealth:
    adapter_factory: Callable[[str], DataPort]

    async def __call__(
        self, request: AddressTxsBalanceRequest
    ) -> AddressTxsBalanceResponse:
        adapter = self.adapter_factory(request.coin)
        address_transactions = await adapter.get_address_transactions(request.address)
        value_in, value_out, difference = 0, 0, 0

        for tx in address_transactions:
            inputs = tx.get("vin")
            outputs = tx.get("vout")

        return AddressTxsBalanceResponse(value_in, value_out, difference)

    async def _calculate_total_inputs_amount(self, inputs: list[dict], address: str):
        value = 0
        for input in inputs:
            if input["prevout"]["scriptpubkey_address"] == address:
                pass
            # TODO: finish calculations

    async def _calculate_total_outputs_amount(self, outputs: list[dict], address: str):
        pass
