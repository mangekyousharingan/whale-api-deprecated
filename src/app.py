from dataclasses import dataclass, field
from typing import Optional

import uvicorn
from fastapi import FastAPI

from adapters.mempool import MempoolSpaceAdapter
from controllers.http import make_http_controller
from ports.DataPort import DataPort
from core.usecases.address_txs_balance_sheet import AddressTxBalance
from core.usecases.address_wealth import AddressWealth


@dataclass
class WhaleAPI:
    http_controller: Optional[FastAPI] = None
    config: dict = field(default_factory=dict)
    adapters: dict = field(default_factory=dict)
    env: Optional[str] = None

    def load_config(self) -> None:
        print("Loading config...")

    def load_adapters(self) -> None:
        self.adapters = {"btc": MempoolSpaceAdapter()}

    def _adapters_factory(self, coin: str) -> DataPort:
        try:
            adapter = self.adapters[coin]
        except KeyError as error:
            raise Exception(f"Adapter for {coin} is not supported!")
        else:
            return adapter

    def set_up(self) -> None:
        address_wealth_usecase = AddressWealth(self._adapters_factory)
        address_tz_balance_usecase = AddressTxBalance(self._adapters_factory)
        self.http_controller = make_http_controller(
            address_wealth_usecase, address_tz_balance_usecase
        )

    def start_service(self) -> None:
        print("Starting service...")
        uvicorn.run(self.http_controller, port=8080, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.load_adapters()
        self.set_up()
        self.start_service()


#  TODO: fix mypy issues
#  TODO: implement other use cases
#  TODO: auth
#  TODO: adapters factory
#  TODO: exception handling
