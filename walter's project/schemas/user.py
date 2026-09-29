from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    """
    Schema for creating a new officer profile.
    """

    national_id: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=1, max_length=50)
    basic_salary: float = Field(..., ge=0 ,description="Basic salary must be non-negative")
    extra_income: float = Field(..., ge=0, description="Extra income must be non-negative")
