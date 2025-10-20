from insurance.domain.policy import InsurancePolicy
from uuid import uuid4
import pytest
import datetime

def test_policy_model_should_validate_fields():
    policy = InsurancePolicy(
        id = 1,
        uuid =uuid4(),
        holder="John Doe",
        hcoverage_amount=100000,
        premium=5000,
        start_date="2023-01-01",
        end_date="2024-01-01"
    )
    assert policy.policy_holder_name == "John Doe"
    assert policy.coverage_amount == 100000
    assert policy.premium == 5000
    assert start_Date == "2023-01-01"
    assert end_date == "2024-01-01"