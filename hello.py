# Recursive Fibonacci and its time complexity

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example
n = 10
print("Fibonacci number:", fibonacci(n))

# Time Complexity:
# The recursive Fibonacci function makes two recursive calls
# for most values of n, so its time complexity is O(2^n).
print("Time Complexity: O(2^n)")

# Space Complexity:
# The maximum recursion depth is n, so the space complexity is O(n).
print("Space Complexity: O(n)")
