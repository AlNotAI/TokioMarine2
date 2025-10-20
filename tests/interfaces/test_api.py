from fastapi.testclient import TestClient
from insurance.interfaces.api import app
from uuid import UUID

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


def test_api_get_policy_by_uuid(monkeypatch):
    test_uuid = UUID("123e4567-e89b-12d3-a456-426614174000")

    monkeypatch.setattr(
        "insurance.interfaces.api.get_policy_by_uuid",
        lambda uuid: type(
            "MockPolicy",
            (),
            {
                "dict": lambda self: {"uuid": str(uuid), "policy_holder_name": "Alice"}
            },
        )()
        if str(uuid) == str(test_uuid)
        else None,
    )

    response = client.get(f"/api/policies/{test_uuid}")
    assert response.status_code == 200
    data = response.json()
    assert data["policy_holder_name"] == "Alice"
    assert data["uuid"] == str(test_uuid)

    response_not_found = client.get("/api/policies/non-existent-uuid")
    assert response_not_found.status_code == 404