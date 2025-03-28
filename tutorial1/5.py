import math
a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
d = b**2 - 4*a*c
if d < 0:
    print("No Real Roots")
else:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots: {root1}, {root2}")