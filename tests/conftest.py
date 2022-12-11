from fastapi import FastAPI
from pytest import fixture
from starlette.testclient import TestClient

from src.app import WhaleAPI
from src.controllers.http import make_http_controller
from src.core.usecases.address_wealth import AddressWealth


@fixture
def app() -> FastAPI:
    address_wealth_usecases = AddressWealth(WhaleAPI.adapters_factory)
    app = make_http_controller(address_wealth_usecases)
    return app


@fixture
def client(app: FastAPI):
    return TestClient(app)
