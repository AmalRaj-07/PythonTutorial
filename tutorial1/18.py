num = int(input("Enter a number: "))
print("Armstrong Number" if num == sum(int(d)**len(str(num)) for d in str(num)) else "Not Armstrong")