import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello via Python!"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_basic_math():
    assert 1 + 1 == 2

def test_string_operations():
    message = "Hello via Python!"
    assert "Python" in message
    assert len(message) > 0
