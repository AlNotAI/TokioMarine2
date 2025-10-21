from insurance.domain.policy import InsurancePolicy
from insurance.infrastructure.db import fetch_all_policies, fetch_policy_by_uuid


def get_all_policies():
    rows = fetch_all_policies()
    return [
        InsurancePolicy(
            id=row[0],
            uuid=row[1],  # Assuming UUID is generated elsewhere
            item=row[2],
            policy_holder_name=row[3],
            hcoverage_amount=row[4],
            premium=row[5],
            start_date=row[6],
            end_date=row[7],
        )
        for row in rows
    ]


def get_policy_by_uuid(uuid):
    row = fetch_policy_by_uuid(uuid)
    if row:
        return InsurancePolicy(
            id=row[0],
            uuid=row[1],
            item=row[2],
            policy_holder_name=row[3],
            hcoverage_amount=row[4],
            premium=row[5],
            start_date=row[6],
            end_date=row[7],
        )
    return None