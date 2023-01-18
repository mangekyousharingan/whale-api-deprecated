from dataclasses import dataclass

import requests

from src.core.models.responses import (AddressTxsBalanceResponse,
                                       AddressWealthResponse)
from src.core.ports.DataPort import DataPort


@dataclass
class MempoolSpaceAdapter(DataPort):
    url: str = "https://mempool.space"

    async def get_address_wealth(self, address: str) -> AddressWealthResponse:
        response = requests.get(f"{self.url}/api/address/{address}/utxo")
        if not response.ok:
            raise Exception("Failed when getting address utxo from Mempool API")

        response_json = response.json()
        address_utxo = await self._sum_utxo(response_json)
        return AddressWealthResponse(address, address_utxo)

    async def _sum_utxo(self, address_data: list[dict], satoshi: bool = False) -> float:
        #  TODO: make conversion to satoshi generic
        total = 0
        for utxo in address_data:
            total += utxo["value"]

        if not satoshi:
            total /= 10**8
        return total

    async def get_address_transactions(self, address: str) -> AddressTxsBalanceResponse:
        response = requests.get(f"{self.url}/api/address/{address}")
        if not response.ok:
            raise Exception("Failed when getting address txs from Mempool API")

        response_json = response.json()
        chain_stats = response_json["chain_stats"]

        address_balance_response = AddressTxsBalanceResponse(
            value_in=chain_stats["funded_txo_sum"],
            value_out=chain_stats["spent_txo_sum"],
            txs=chain_stats["tx_count"],
            difference=chain_stats["funded_txo_sum"] - chain_stats["spent_txo_sum"],
        )

        return address_balance_response
