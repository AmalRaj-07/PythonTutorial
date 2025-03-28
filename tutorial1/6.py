a, b, c = sorted(map(int, input("Enter sides of triangle: ").split()))
print("Right-angled Triangle" if a**2 + b**2 == c**2 else "Not a Right-angled Triangle")