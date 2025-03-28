import math
x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())
print(f"Distance: {math.sqrt((x2-x1)**2 + (y2-y1)**2)}")