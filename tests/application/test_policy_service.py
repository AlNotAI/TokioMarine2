from insurance.application.policy_service import get_all_policies, get_policy_by_uuid
from insurance.domain.policy import InsurancePolicy
from datetime import date
from uuid import UUID


def test_get_all_policies_with_stubbed_data(monkeypatch):
    monkeypatch.setattr(
        "insurance.application.policy_service.fetch_all_policies",
        lambda: [
            (
                1,
                UUID("urn:uuid:12345678-1234-5678-1234-567812345678"),
                "Alice",
                100000,
                5000,
                date(2023, 1, 1),
                date(2024, 1, 1),
            ),
            (
                2,
                UUID("urn:uuid:12345678-1234-5678-1234-567812345679"),
                "Bob",
                200000,
                10000,
                date(2023, 6, 1),
                date(2024, 6, 1),
            ),
        ],
    )
    policies = get_all_policies()
    assert isinstance(policies, list)
    assert len(policies) == 2
    assert isinstance(policies[0], InsurancePolicy)
    assert policies[0].id == 1
    assert policies[0].policy_holder_name == "Alice"
    assert policies[0].coverage_amount == 100000
    assert policies[0].premium == 5000
    assert policies[0].start_date == date(2023, 1, 1)
    assert policies[0].end_date == date(2024, 1, 1)



def test_get_policy_by_uuid_with_stubbed_data(monkeypatch):
    test_uuid = UUID("urn:uuid:12345678-1234-5678-1234-567812345678")
    monkeypatch.setattr(
        "insurance.application.policy_service.fetch_policy_by_uuid",
        lambda uuid: (1, uuid, "Alice", 100000, 5000, date(2023, 1, 1), date(2024, 1, 1))
    )
    policy = get_policy_by_uuid(test_uuid)
    assert policy.policy_holder_name == "Alice"
    assert policy.coverage_amount == 100000
    assert policy.premium == 5000
    assert policy.start_date == date(2023, 1, 1)
    assert policy.end_date == date(2024, 1, 1)
    assert policy.uuid == test_uuid