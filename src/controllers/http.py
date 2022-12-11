import dataclasses

from fastapi import FastAPI, Response
from starlette.responses import JSONResponse

from src.core.models.requests import AddressWealthRequest
from src.core.usecases.address_wealth import AddressWealth


def make_http_controller(address_wealth_usecase: AddressWealth) -> FastAPI:

    controller = FastAPI()

    @controller.get("/")
    async def heartbeat() -> Response:
        return Response("OK")

    @controller.get("/api/v1/{coin}/address/{address}")
    async def address_wealth(address: str, coin: str) -> JSONResponse:
        usecase_request = AddressWealthRequest(coin.lower(), address)
        response = await address_wealth_usecase(usecase_request)
        return JSONResponse(content=dataclasses.asdict(response))

    return controller
