from fastapi.testclient import TestClient
from insurance.interfaces.api import app

client = TestClient(app)

def test_get_all_policies(monkeypatch):
    monkeypatch.setattr(
        "insurance.interfaces.api.get_all_policies",
        lambda: [
            type("MockPolicy", (), {"dict": lambda self: {"policy_holder_name": "Alice"}})(),
            type("MockPolicy", (), {"dict": lambda self: {"policy_holder_name": "Bob"}})()
        ]
    )

    response = client.get("/api/policies/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["policy_holder_name"] == "Alice"
    assert data[1]["policy_holder_name"] == "Bob"