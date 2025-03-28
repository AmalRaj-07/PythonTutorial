def separate_data_types(lst):
    integers, floats, strings = [], [], []
    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, float):
            floats.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, floats, strings
data = [1, 2.5, "apple", 3, 4.7, "banana", 10]
integers, floats, strings = separate_data_types(data)
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)