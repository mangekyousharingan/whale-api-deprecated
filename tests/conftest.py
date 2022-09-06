from fastapi import FastAPI
from pytest import fixture
from starlette.testclient import TestClient

from src.controllers.http import make_http_controller


@fixture
def app() -> FastAPI:
    app = make_http_controller()
    return app


@fixture
def client(app: FastAPI):
    return TestClient(app)

