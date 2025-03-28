from collections import Counter
def remove_all_duplicates(lst):
    count = Counter(lst)
    return [item for item in lst if count[item] == 1]
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List after completely removing duplicates:", remove_all_duplicates(nums))