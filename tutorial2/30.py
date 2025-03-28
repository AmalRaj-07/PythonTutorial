def remove_duplicates(lst):
    return list(set(lst))
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List without duplicates:", remove_duplicates(nums))