def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def separate_numbers(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if not is_prime(num) and num > 1]
    return primes, composites
nums = list(map(int, input("Enter positive integers separated by spaces: ").split()))
primes, composites = separate_numbers(nums)
print("Prime numbers:", primes)
print("Composite numbers:", composites)