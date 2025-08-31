import pytest
import math
from app.services import calculate_future_value, calculate_required_rate

class TestServices:
    """ Test class for service calculations. """
    
    def setup_method(self, method):
        """Setup method that runs before each test."""
        print(f"\n=== Starting test: {method.__name__} ===")

    def teardown_method(self, method):
        """Teardown method that runs after each test."""
        print(f"=== Completed test: {method.__name__} ===\n")
        
    def test_calculate_future_value_basic(self):
        """Debug test for back future value calcuation."""
        # Test data from your README example
        P = 10000 # Principal
        R = 0.040753 # Interest Rate
        N = 4 # Compounding periods per year
        T = 10 # Time in years

        print(f"DEBUG: Input values:")
        print(f"  P (Principal): {P}")
        print(f"  R (Interest Rate): {R} ({R*100}%)")
        print(f"  N (Compounding Periods): {N}")
        print(f"  T (Time in Years): {T}")

        # Calculate step by step for debugging
        print(f"\nDEBUG: Step-by-step calculation:")
        step1 = R / N
        print(f"  Step 1: R/N = {R}/{N} = {step1}")
        
        step2 = 1 + step1
        print(f"  Step 2: 1 + (R/N) = 1 + {step1} = {step2}")
        
        step3 = N * T
        print(f"  Step 3: N*T = {N}*{T} = {step3}")
        
        step4 = step2 ** step3
        print(f"  Step 4: (1 + R/N)^(N*T) = {step2}^{step3} = {step4}")
        
        step5 = P * step4
        print(f"  Step 5: P * (1 + R/N)^(N*T) = {P} * {step4} = {step5}")
        
        # Call the function
        result = calculate_future_value(P, R, N, T)
        print(f"\nDEBUG: Function result: {result}")
        print(f"DEBUG: Expected result: {round(step5, 2)}")
        print(f"DEBUG: Results match: {result == round(step5, 2)}")
        
        # Assertions
        assert result == round(step5, 2)
        assert result > P  # Future value should be greater than principal
        assert isinstance(result, float)

    def test_calculate_future_value_edge_cases(self):
        """Debug test for edge cases in future value calculation."""
        test_cases = [
            {
                "name": "Zero interest rate",
                "P": 1000, "R": 0.0, "N": 1, "T": 5,
                "expected": 1000.0
            },
            {
                "name": "High interest rate",
                "P": 1000, "R": 0.50, "N": 12, "T": 1,
                "expected": 1000 * (1 + 0.50/12) ** (12 * 1)
            },
            {
                "name": "Daily compounding",
                "P": 1000, "R": 0.05, "N": 365, "T": 1,
                "expected": 1000 * (1 + 0.05/365) ** (365 * 1)
            },
            {
                "name": "Long time period",
                "P": 1000, "R": 0.05, "N": 1, "T": 50,
                "expected": 1000 * (1 + 0.05/1) ** (1 * 50)
            }
        ]
        
        for test_case in test_cases:
            print(f"\nDEBUG: Testing {test_case['name']}")
            print(f"DEBUG: Input: P={test_case['P']}, R={test_case['R']}, N={test_case['N']}, T={test_case['T']}")
            
            result = calculate_future_value(
                test_case['P'], 
                test_case['R'], 
                test_case['N'], 
                test_case['T']
            )
            
            expected = round(test_case['expected'], 2)
            print(f"DEBUG: Result: {result}")
            print(f"DEBUG: Expected: {expected}")
            print(f"DEBUG: Match: {result == expected}")
            
            assert result == expected
    
    def test_calculate_required_rate_basic(self):
        """Debug test for basic required rate calculation."""
        # Use the reverse of the future value example
        FV = 15000  # Future value
        P = 10000   # Principal
        N = 4       # Compounding periods per year
        T = 10      # Time in years
        
        print(f"DEBUG: Input values:")
        print(f"  FV (Future Value): {FV}")
        print(f"  P (Principal): {P}")
        print(f"  N (Compounding Periods): {N}")
        print(f"  T (Time in Years): {T}")
        
        # Calculate step by step for debugging
        print(f"\nDEBUG: Step-by-step calculation:")
        step1 = FV / P
        print(f"  Step 1: FV/P = {FV}/{P} = {step1}")
        
        step2 = N * T
        print(f"  Step 2: N*T = {N}*{T} = {step2}")
        
        step3 = 1 / step2
        print(f"  Step 3: 1/(N*T) = 1/{step2} = {step3}")
        
        step4 = step1 ** step3
        print(f"  Step 4: (FV/P)^(1/(N*T)) = {step1}^{step3} = {step4}")
        
        step5 = step4 - 1
        print(f"  Step 5: base - 1 = {step4} - 1 = {step5}")
        
        step6 = N * step5
        print(f"  Step 6: N * (base - 1) = {N} * {step5} = {step6}")
        
        # Call the function
        result = calculate_required_rate(FV, P, N, T)
        print(f"\nDEBUG: Function result: {result}")
        print(f"DEBUG: Expected result: {round(step6, 6)}")
        print(f"DEBUG: Results match: {abs(result - round(step6, 6)) < 0.000001}")
        
        # Verify by calculating future value with this rate
        verification = calculate_future_value(P, result, N, T)
        print(f"DEBUG: Verification - FV with calculated rate: {verification}")
        print(f"DEBUG: Verification matches target FV: {abs(verification - FV) < 1}")
        
        # Assertions
        assert abs(result - round(step6, 6)) < 0.000001
        assert result > 0  # Interest rate should be positive
        assert isinstance(result, float)
    
    def test_calculate_required_rate_edge_cases(self):
        """Debug test for edge cases in required rate calculation."""
        test_cases = [
            {
                "name": "Same principal and future value",
                "FV": 1000, "P": 1000, "N": 1, "T": 1,
                "expected": 0.0
            },
            {
                "name": "High growth target",
                "FV": 2000, "P": 1000, "N": 1, "T": 1,
                "expected": 1.0  # 100% interest rate
            },
            {
                "name": "Long time period",
                "FV": 2000, "P": 1000, "N": 1, "T": 10,
                "expected": 0.071773  # Approximately 7.18%
            }
        ]
        
        for test_case in test_cases:
            print(f"\nDEBUG: Testing {test_case['name']}")
            print(f"DEBUG: Input: FV={test_case['FV']}, P={test_case['P']}, N={test_case['N']}, T={test_case['T']}")
            
            result = calculate_required_rate(
                test_case['FV'], 
                test_case['P'], 
                test_case['N'], 
                test_case['T']
            )
            
            expected = test_case['expected']
            print(f"DEBUG: Result: {result}")
            print(f"DEBUG: Expected: {expected}")
            print(f"DEBUG: Difference: {abs(result - expected)}")
            print(f"DEBUG: Match: {abs(result - expected) < 0.000001}")
            
            assert abs(result - expected) < 0.000001
    
    def test_calculate_required_rate_error_handling(self):
        """Debug test for error handling in required rate calculation."""
        error_cases = [
            {
                "name": "Negative principal",
                "FV": 1000, "P": -1000, "N": 1, "T": 1,
                "expected_error": ValueError
            },
            {
                "name": "Zero principal",
                "FV": 1000, "P": 0, "N": 1, "T": 1,
                "expected_error": ValueError
            },
            {
                "name": "Negative future value",
                "FV": -1000, "P": 1000, "N": 1, "T": 1,
                "expected_error": ValueError
            },
            {
                "name": "Zero compounding periods",
                "FV": 1000, "P": 1000, "N": 0, "T": 1,
                "expected_error": ValueError
            },
            {
                "name": "Zero time period",
                "FV": 1000, "P": 1000, "N": 1, "T": 0,
                "expected_error": ValueError
            }
        ]
        
        for test_case in error_cases:
            print(f"\nDEBUG: Testing error case: {test_case['name']}")
            print(f"DEBUG: Input: FV={test_case['FV']}, P={test_case['P']}, N={test_case['N']}, T={test_case['T']}")
            
            try:
                result = calculate_required_rate(
                    test_case['FV'], 
                    test_case['P'], 
                    test_case['N'], 
                    test_case['T']
                )
                print(f"DEBUG: Unexpected success - got result: {result}")
                assert False, f"Expected {test_case['expected_error']} but got result {result}"
            except test_case['expected_error'] as e:
                print(f"DEBUG: Correctly raised {test_case['expected_error'].__name__}: {str(e)}")
                assert "Invalid input" in str(e)
    
    def test_round_trip_verification(self):
        """Debug test to verify calculations work in both directions."""
        # Start with known values
        P = 10000
        R = 0.05  # 5%
        N = 4
        T = 10
        
        print(f"DEBUG: Round-trip verification:")
        print(f"DEBUG: Starting values: P={P}, R={R}, N={N}, T={T}")
        
        # Calculate future value
        FV = calculate_future_value(P, R, N, T)
        print(f"DEBUG: Calculated FV: {FV}")
        
        # Calculate required rate to get back to original
        R_calculated = calculate_required_rate(FV, P, N, T)
        print(f"DEBUG: Calculated R: {R_calculated}")
        
        # Verify they match
        print(f"DEBUG: Original R: {R}")
        print(f"DEBUG: Calculated R: {R_calculated}")
        print(f"DEBUG: Difference: {abs(R - R_calculated)}")
        print(f"DEBUG: Match: {abs(R - R_calculated) < 0.000001}")
        
        assert abs(R - R_calculated) < 0.000001
        
        # Verify by calculating FV again
        FV_verification = calculate_future_value(P, R_calculated, N, T)
        print(f"DEBUG: Verification FV: {FV_verification}")
        print(f"DEBUG: Original FV: {FV}")
        print(f"DEBUG: FV Match: {abs(FV - FV_verification) < 0.01}")
        
        assert abs(FV - FV_verification) < 0.01