def set_operations(set1, set2):
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)
    print("Symmetric Difference:", set1 ^ set2)
set1 = set(map(int, input("Enter elements of set1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set2 separated by spaces: ").split()))
set_operations(set1, set2)