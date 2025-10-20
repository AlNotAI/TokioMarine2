from pydantic import BaseModel, Field, field_validator, model_validator
from uuid import UUID
from datetime import date

class InsurancePolicy(BaseModel):
    id: int
    uuid: UUID
    policy_holder_name: str = Field(..., alias="holder")
    coverage_amount: int = Field(..., alias="hcoverage_amount")
    premium: int
    start_date: date
    end_date: date

    @field_validator("coverage_amount")
    def coverage_must_be_non_negative(cls, value):
        if value < 0:
            raise ValueError("coverage_amount must be non-negative")
        return value

    @model_validator(mode="after")
    def end_date_after_start_date(self):
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")
        return self

    model_config = {
        "populate_by_name": True,  # allow constructing with field names as well as aliases
    }