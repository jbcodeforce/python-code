from fastapi.testclient import TestClient
from main import app

def test_read_main():
    client = TestClient(app)
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws/12") as websocket:
        websocket.send_text("Hello from client 12")
        data = websocket.receive_text()
        assert data == "You wrote: Hello from client 12"