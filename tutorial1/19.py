numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Even count: {sum(1 for x in numbers if x % 2 == 0)}")
print(f"Odd count: {sum(1 for x in numbers if x % 2 != 0)}")