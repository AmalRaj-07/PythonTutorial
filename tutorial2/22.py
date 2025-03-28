text = input("Enter the string: ")
words_to_remove = input("Enter words to remove separated by spaces: ").split()
for word in words_to_remove:
    text = text.replace(word, "")
print("Resulting string:", text.strip())