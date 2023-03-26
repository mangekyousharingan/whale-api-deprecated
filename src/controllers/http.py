import dataclasses

from fastapi import FastAPI, Response
from starlette.responses import JSONResponse

from core.models.requests import (AddressTxsBalanceRequest,
                                      AddressWealthRequest)
from core.usecases.address_txs_balance_sheet import AddressTxBalance
from core.usecases.address_wealth import AddressWealth


def make_http_controller(
    address_wealth_usecase: AddressWealth, address_balance_usecase: AddressTxBalance
) -> FastAPI:

    controller = FastAPI()

    @controller.get("/healthz")
    async def heartbeat() -> Response:
        return Response("OK")

    @controller.get("/api/v1/{coin}/address/{address}")
    async def address_wealth(address: str, coin: str) -> JSONResponse:
        usecase_request = AddressWealthRequest(coin.lower(), address)
        response = await address_wealth_usecase(usecase_request)
        return JSONResponse(content=dataclasses.asdict(response))

    @controller.get("/api/v1/{coin}/address/{address}/balance")
    async def address_wealth(address: str, coin: str) -> JSONResponse:
        usecase_request = AddressTxsBalanceRequest(coin.lower(), address)
        response = await address_balance_usecase(usecase_request)
        return JSONResponse(content=dataclasses.asdict(response))

    return controller
