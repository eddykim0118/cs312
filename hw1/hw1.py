def fabonacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return fabonacci(n - 1) + fabonacci(n - 2) * fabonacci(n - 3)

# Example usage:
n = 5
print(f"fabonacci({n}) =", fabonacci(n))
