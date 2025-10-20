from insurance.domain.policy import InsurancePolicy
from uuid import uuid4
import pytest
import datetime


def test_policy_model_should_validate_fields():
    policy = InsurancePolicy(
        id=1,
        uuid=uuid4(),
        holder="John Doe",
        hcoverage_amount=100000,
        premium=5000,
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2024, 1, 1),
    )
    assert policy.policy_holder_name == "John Doe"
    assert policy.coverage_amount == 100000
    assert policy.premium == 5000
    assert policy.start_date == datetime.date(2023, 1, 1)
    assert policy.end_date == datetime.date(2024, 1, 1)


def test_policy_model_should_raise_validation_error_for_negative_coverage():
    with pytest.raises(ValueError):
        InsurancePolicy(
            id=2,
            uuid=uuid4(),
            holder="Jane Doe",
            hcoverage_amount=-50000,
            premium=3000,
            start_date=datetime.date(2023, 1, 1),
            end_date=datetime.date(2024, 1, 1),
        )
