import logging
import time
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

# Get logger for this module
logger = logging.getLogger(__name__)

# Configure api rouer for application
router = APIRouter()


@router.post("/future-value", response_model=FutureValueResponse)
def future_value(request: FutureValueRequest) -> FutureValueResponse:
    start_time = time.time()
    logger.info(f"Received Future-value request: P={request.P}, R={request.R}, N={request.N}, T={request.T}")

    try:
        future_value = calculate_future_value(request.P, request.R, request.N, request.T)
        response = FutureValueResponse(message=f"Future Value of {round(future_value)} when starting with {round(request.P)} compounded at {request.R} interest rate, {request.N} times per year over {request.T} years")
        time.sleep(2)
        response_time = time.time() - start_time
        logger.info(f"Future-value calculation completed in {response_time:.4f} seconds")

        logger.info(f"Future-value response: {response}")
        return response
    except ValueError as e:
        response_time = time.time() - start_time
        logger.error(f"Future-value calculation failed after {response_time:.4f} seconds: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/required-rate", response_model=RequiredRateResponse)
def required_rate(request: RequiredRateRequest) -> RequiredRateResponse:
    start_time = time.time()
    logger.info(f"Received Required-rate request: P={request.P}, FV={request.FV}, N={request.N}, T={request.T}")
    
    try:
        required_rate = calculate_required_rate(request.FV, request.P, request.N, request.T)
        response = RequiredRateResponse(message=f"{round(required_rate * 100, 2)}% is the required interest rate to grow ${round(request.P)} to ${round(request.FV)} if compounding {request.N} times per year over {request.T} years.")

        response_time = time.time() - start_time
        logger.info(f"Required-rate calculation completed in {response_time:.4f} seconds")

        logger.info(f"Required-rate response: {response}")
        return response
    except ValueError as e:
        response_time = time.time() - start_time
        logger.debug(f"Required-rate calculation failed after {response_time:.4f} seconds: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))