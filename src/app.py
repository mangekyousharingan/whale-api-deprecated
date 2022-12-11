from dataclasses import dataclass, field
from typing import Optional

import uvicorn
from fastapi import FastAPI

from src.adapters.mempool import MempoolSpaceAdapter
from src.controllers.http import make_http_controller
from src.core.ports.DataPort import DataPort
from src.core.usecases.address_wealth import AddressWealth


@dataclass
class WhaleAPI:
    http_controller: Optional[FastAPI] = None
    config: dict = field(default_factory=dict)
    env: Optional[str] = None

    def load_config(self) -> None:
        print("Loading config...")

    @staticmethod
    def adapters_factory(coin: str) -> DataPort:
        adapters = {"btc": MempoolSpaceAdapter()}
        return adapters[coin]

    def set_up(self) -> None:
        address_wealth_usecase = AddressWealth(self.adapters_factory)
        self.http_controller = make_http_controller(address_wealth_usecase)

    def start_service(self) -> None:
        uvicorn.run(self.http_controller, port=80, host="0.0.0.0")

    def set_up_and_start_service(self) -> None:
        self.load_config()
        self.set_up()
        self.start_service()


#  TODO: fix mypy issues
#  TODO: implement other use cases
#  TODO: auth
#  TODO: adapters factory
#  TODO: exception handling
