from insurance.domain.policy import InsurancePolicy


def fetch_all_policies():
    pass  # Placeholder for actual data fetching logic


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
