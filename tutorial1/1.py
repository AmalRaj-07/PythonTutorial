seconds = int(input("Enter time in seconds: "))
print(f"{seconds // 3600:02}:{(seconds % 3600) // 60:02}:{seconds % 60:02}")