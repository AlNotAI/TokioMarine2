from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from insurance.application.policy_service import get_all_policies, get_policy_by_uuid
from dotenv import load_dotenv
load_dotenv()  # loads .env into environment


app = FastAPI(default_response_class=JSONResponse)

# Allow requests from your frontend origin
origins = [
    "http://localhost:3000",  # or whatever port your frontend runs on
]
# add CORS middleware (development: allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # change to specific origins in production e.g. ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _to_dict(obj):
    # If it's a pydantic model
    if hasattr(obj, "dict") and callable(getattr(obj, "dict")):
        return obj.dict()
    # If it's already a mapping/dict
    if isinstance(obj, dict):
        return obj
    # fallback: return object as-is (FastAPI will attempt to serialize)
    return obj

@app.get("/api/policies/")
def read_policies():
    # return [policy.dict() for policy in get_all_policies()]
    return _to_dict([policy for policy in get_all_policies()])


@app.get("/api/policies/{uuid}")
def read_policy(uuid: str):
    policy = get_policy_by_uuid(uuid)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    # return policy.dict()
    return _to_dict(policy)