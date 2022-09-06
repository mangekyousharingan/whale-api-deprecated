from fastapi import FastAPI, Response


def make_http_controller() -> FastAPI:

    controller = FastAPI()

    @controller.get("/")
    async def heartbeat() -> Response:
        return Response("OK")

    return controller
