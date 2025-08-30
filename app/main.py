from fastapi import FastAPI
from .routers import router

app = FastAPI(title="Compound Interest Calculator", description="Calculate the future value of an investment or the required interest rate to reach a future value")

app.include_router(router)