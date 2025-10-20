from fastapi import FastAPI, HTTPException

def get_all_policies():
    # Placeholder for actual implementation
    pass
def get_policy_by_uuid(uuid):
    # Placeholder for actual implementation
    pass

app = FastAPI()

@app.get("/api/policies/")
def read_policies():
    return [policy.dict() for policy in get_all_policies()]