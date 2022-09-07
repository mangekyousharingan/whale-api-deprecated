import dataclasses

from fastapi import FastAPI, Response
from starlette.responses import JSONResponse

from src.adapters.mempool import get_address_utxo


def make_http_controller() -> FastAPI:

    controller = FastAPI()

    @controller.get("/")
    async def heartbeat() -> Response:
        return Response("OK")

    @controller.get("/api/v1/address/{address}/utxo")
    async def address_utxo(address: str) -> JSONResponse:
        response = await get_address_utxo(address)
        return JSONResponse(content=dataclasses.asdict(response))

    return controller
