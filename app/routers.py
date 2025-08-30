from fastapi import APIRouter, HTTPException
from .models import (
    FutureValueRequest,
    FutureValueResponse,
    RequiredRateRequest,
    RequiredRateResponse,
)
from .services import (
    calculate_future_value,
    calculate_required_rate,
)

router = APIRouter()

@router.post("/future-value", response_model=FutureValueResponse)
def future_value(request: FutureValueRequest) -> FutureValueResponse:
    
    try:
        future_value = calculate_future_value(request.P, request.R, request.N, request.T)
        return FutureValueResponse(message=f"Future Value of {round(future_value)} when starting with {round(request.P)} compounded at {request.R} interest rate, {request.N} times per year over {request.T} years")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return FutureValueResponse(message=f"Future Value of {calculate_future_value(request.P, request.R, request.N, request.T)} when starting with {request.P} compounded at {request.R} interest rate, {request.N} times per year over {request.T} years")

@router.post("/required-rate", response_model=RequiredRateResponse)
def required_rate(request: RequiredRateRequest) -> RequiredRateResponse:
    try:
        required_rate = calculate_required_rate(request.FV, request.P, request.N, request.T)
        return RequiredRateResponse(message=f"{round(required_rate * 100, 2)}% is the required interest rate to grow ${round(request.P)} to ${round(request.FV)} if compounding {request.N} times per year over {request.T} years.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))