"""
    Compound interest formula: 
    FV = P * (1 + R/N) ** (N * T)
"""
def calculate_future_value(P: float, R: float, N: int, T: int) -> float:
    return round(P * (1 + R / N) ** (N * T), 2)
    
"""
    Rearranged compound interest formula:
    FV = P * (1 + R/N) ** (N * T)
    Solve for R
"""
def calculate_required_rate(FV: float, P: float, N: int, T: int) -> float:
    if P <= 0 or FV <= 0 or N <= 0 or T <= 0:
        raise ValueError("Invalid input: P, FV, N, and T must be greater than 0")
    
    base = (FV / P) ** (1 / (N * T))
    R = N * (base - 1)
    
    return round(R, 6) # Keep precision for interest rate

