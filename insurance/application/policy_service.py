from insurance.domain.policy import InsurancePolicy
from insurance.infrastructure.db import fetch_all_policies, fetch_policy_by_uuid


# def fetch_all_policies():
#     pass  # Placeholder for actual data fetching logic
# def fetch_policy_by_uuid(uuid):
#     pass  # Placeholder for actual data fetching logic

def get_all_policies():
    rows = fetch_all_policies()
    return [
        InsurancePolicy(
            id=row[0],
            uuid=row[1],  # Assuming UUID is generated elsewhere
            holder=row[2],
            hcoverage_amount=row[3],
            premium=row[4],
            start_date=row[5],
            end_date=row[6],
        )
        for row in rows
    ]


def get_policy_by_uuid(uuid):
    row = fetch_policy_by_uuid(uuid)
    if row:
        return InsurancePolicy(
            id=row[0],
            uuid=row[1],
            holder=row[2],
            hcoverage_amount=row[3],
            premium=row[4],
            start_date=row[5],
            end_date=row[6],
        )
    return None