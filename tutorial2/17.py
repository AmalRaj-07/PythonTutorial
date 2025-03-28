import math
def sin_series(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result
x = float(input("Enter value of x in radians: "))
n = int(input("Enter number of terms: "))
print(f"sin({x}) ≈ {sin_series(x, n)}")