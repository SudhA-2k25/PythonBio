# Fibonacci series

def fibonacci_series(n):
    # Initialize var
    a, b = 0, 1
    
    # series
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_series(5):
    print(num)