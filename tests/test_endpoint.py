from starlette.testclient import TestClient


def test_health(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "OK"

