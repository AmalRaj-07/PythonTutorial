nums = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
pos = [x for x in nums if x > 0]
neg = [x for x in nums if x < 0]
print(f"Positive Sum: {sum(pos)}, Average: {sum(pos)/len(pos)}")
print(f"Negative Sum: {sum(neg)}, Average: {sum(neg)/len(neg)}")