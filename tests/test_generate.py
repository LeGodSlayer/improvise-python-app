# tests/test_generate.py
# Run tests with: pytest -q

from fastapi.testclient import TestClient
from main import app
import hashlib

client = TestClient(app)


def test_health():
    """Test the /health endpoint"""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_generate_checksum_success():
    """Test /generate with a valid text payload"""
    payload = {"text": "hello world"}
    r = client.post("/generate", json=payload)
    assert r.status_code == 200
    body = r.json()

    # check response contains required fields
    assert "checksum_sha256" in body
    assert "original_text" in body
    assert "welcome" in body

    # verify checksum is correct
    expected = hashlib.sha256(payload["text"].encode("utf-8")).hexdigest()
    assert body["checksum_sha256"] == expected
    assert body["original_text"] == payload["text"]


def test_generate_bad_request():
    """Test /generate with invalid payloads"""

    # missing text field
    r = client.post("/generate", json={})
    assert r.status_code == 422  # Pydantic validation error

    # text not a string
    r2 = client.post("/generate", json={"text": 123})
    assert r2.status_code == 422
