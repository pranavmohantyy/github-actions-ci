from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    resp = client.get("/add", params={"x": 1, "y": 2})
    assert resp.status_code == 200
    assert resp.json() == {"result": 3}

def test_subtract():
    resp = client.get("/subtract", params={"x": 5, "y": 3})
    assert resp.status_code == 200
    assert resp.json() == {"result": 2}

def test_multiply():
    resp = client.get("/multiply", params={"x": 3, "y": 4})
    assert resp.status_code == 200
    assert resp.json() == {"result": 12}

def test_divide():
    resp = client.get("/divide", params={"x": 10, "y": 2})
    assert resp.status_code == 200
    assert resp.json() == {"result": 5}
