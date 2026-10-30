from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_question_too_short_is_rejected():
    response = client.post("/ask", json={"question": "abc"})
    assert response.status_code == 422

def test_blank_question_is_rejected():
    response = client.post("/ask", json={"question": "     "})
    assert response.status_code == 422

def test_missing_question_is_rejected():
    response = client.post("/ask", json={})
    assert response.status_code == 422

def test_question_over_limit_is_rejected():
    response = client.post("/ask", json={"question": "x" * 2001})
    assert response.status_code == 422
