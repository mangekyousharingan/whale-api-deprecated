from dataclasses import dataclass

import requests


@dataclass
class AddressUtxoResponse:
    address: str
    utxo: float


async def get_address_utxo(address: str) -> AddressUtxoResponse:
    url = f"https://mempool.space/api/address/{address}/utxo"
    response = requests.get(url)
    response_json = response.json()
    address_utxo = sum_utxo(response_json)
    return AddressUtxoResponse(address, address_utxo)


def sum_utxo(address_data: list[dict]) -> float:
    total = 0
    for utxo in address_data:
        total += utxo["value"]

    total /= 10 ** 8
    return total
