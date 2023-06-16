# taylor series
import math

def taylor_series(x, n):
    sum = 0
    term = 1
    
    # Calculate each term and add to sum
    for i in range(1, n+1):
        term *= x / i
        sum += term
    return sum


x = 2.0
n = 5
sin_x =round( taylor_series(x, n),3)
actual_value=round(math.sin(x),3)
print(f"sin({x}) using {n} terms of Taylor series = {sin_x}")
print(f"Actual value of sin({x}) = {actual_value}")
