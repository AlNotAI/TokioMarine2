from typing import List, Optional
from insurance.domain.policy import InsurancePolicy
from insurance.infrastructure.db import fetch_all_policies, fetch_policy_by_uuid


def get_all_policies() -> List[InsurancePolicy]:
    """
    Load all policy rows from the infrastructure layer and convert them to
    InsurancePolicy domain models.

    The infrastructure layer is expected to return an iterable of rows where
    columns are ordered as:
      (id, uuid, item, policy_holder_name, coverage_amount, premium, start_date, end_date)

    Returns:
        List[InsurancePolicy]: A list of validated InsurancePolicy instances.
    Raises:
        Propagates any exceptions raised by fetch_all_policies or by model validation.
    """
    rows = fetch_all_policies()
    return [
        InsurancePolicy(
            id=row[0],
            uuid=row[1],
            item=row[2],
            policy_holder_name=row[3],
            coverage_amount=row[4],
            premium=row[5],
            start_date=row[6],
            end_date=row[7],
        )
        for row in rows
    ]


def get_policy_by_uuid(uuid) -> Optional[InsurancePolicy]:
    """
    Load a single policy identified by uuid and convert it to an InsurancePolicy.

    Args:
        uuid: UUID or string identifying the policy.

    Returns:
        InsurancePolicy if a matching row is found, otherwise None.

    Notes:
        The returned object is a single InsurancePolicy (not a list). If the
        database row uses string/date types they must be compatible with the
        InsurancePolicy field types or validation will raise.
    """
    row = fetch_policy_by_uuid(uuid)
    if row:
        return InsurancePolicy(
            id=row[0],
            uuid=row[1],
            item=row[2],
            policy_holder_name=row[3],
            coverage_amount=row[4],
            premium=row[5],
            start_date=row[6],
            end_date=row[7],
        )
    return None