n = int(input("Enter number of values: "))
numbers = list(map(int, input("Enter numbers: ").split()))
print(f"Sum of even numbers: {sum(x for x in numbers if x % 2 == 0)}")