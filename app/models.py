from pydantic import BaseModel, Field

class FutureValueRequest(BaseModel):
    P: float = Field(..., gt=0, description="Principal amount")
    R: float = Field(..., gt=0, description="Annual interest rate (decimal)")
    N: int = Field(..., gt=0,description="Compounding periods per year")
    T: int = Field(..., gt=0, description="Total time in years")

class FutureValueResponse(BaseModel):
    message: str = Field(..., description="Message indicating the future value")

class RequiredRateRequest(BaseModel):
    FV: float = Field(..., gt=0, description="Future value")
    P: float = Field(..., gt=0, description="Principal amount")
    N: int = Field(..., gt=0, description="Compounding periods per year")
    T: int = Field(..., gt=0, description="Total time in years")

class RequiredRateResponse(BaseModel):
    message: str = Field(..., description="Message indicating the required interest rate")