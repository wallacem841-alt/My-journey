def fibonacci_calc(start, second, x):
    if x <= 0:
        return start  # Base case returning the correct Fibonacci number
    if x == 1:
        return second  # Base case for the next Fibonacci number
    
    temp = start + second

    return fibonacci_calc(second, temp, x - 1)  # Recursive call with updated values

# Test the function for the 8th Fibonacci number (starting from index 0)
result = fibonacci_calc(0, 1, 8)
print(result)
