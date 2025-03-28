low, high = map(int, input("Enter lower and upper limit: ").split())
print(sum(x for x in range(low, high+1) if x % 2 != 0))