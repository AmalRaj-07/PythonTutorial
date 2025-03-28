def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Median:", find_median(nums))