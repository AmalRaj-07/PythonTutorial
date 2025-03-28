from collections import Counter
def find_mode(numbers):
    count = Counter(numbers)
    mode = [key for key, value in count.items() if value == max(count.values())]
    return mode
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Mode:", find_mode(nums))