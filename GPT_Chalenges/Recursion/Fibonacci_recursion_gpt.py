def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
    
result = fibonacci(8)
print(result)