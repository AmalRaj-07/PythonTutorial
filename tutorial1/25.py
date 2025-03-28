x, y = map(int, input("Enter X and Y: ").split())
result = 1
for _ in range(y):
    result *= x
print(result)