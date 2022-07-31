from starlette.testclient import TestClient


def test_health(client: TestClient):
    response = client.get("/")
    assert response.json() == {"healthy": True}
