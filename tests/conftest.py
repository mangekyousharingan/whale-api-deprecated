from fastapi import FastAPI
from pytest import fixture
from starlette.testclient import TestClient
from src.main import app


app = TestClient(app)


@fixture
def client():
    return app
