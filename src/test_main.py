import pytest
from main import app

def test_index():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.get("/")
    assert b"Hello" in response.data
