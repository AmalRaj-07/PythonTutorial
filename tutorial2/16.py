def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
def generate_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]
while True:
    print("\nMenu:")
    print("1. Check Even or Odd")
    print("2. Check Positive, Negative, or Zero")
    print("3. Generate Factors")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4:
        break
    num = int(input("Enter a number: "))
    if choice == 1:
        print(is_even_or_odd(num))
    elif choice == 2:
        print(check_number(num))
    elif choice == 3:
        print("Factors:", generate_factors(num))
    else:
        print("Invalid choice!")