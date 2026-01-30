numbers = [1, 2, 2, 3, 3, 3]

counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

print(counts)
