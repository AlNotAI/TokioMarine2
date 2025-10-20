from fastapi import FastAPI, HTTPException
from insurance.application.policy_service import get_all_policies, get_policy_by_uuid

# def get_all_policies():
#     # Placeholder for actual implementation
#     pass
# def get_policy_by_uuid(uuid):
#     # Placeholder for actual implementation
#     pass

app = FastAPI()

@app.get("/api/policies/")
def read_policies():
    return [policy.dict() for policy in get_all_policies()]


@app.get("/api/policies/{uuid}")
def read_policy(uuid: str):
    policy = get_policy_by_uuid(uuid)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy.dict()