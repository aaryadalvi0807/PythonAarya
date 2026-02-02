words = ["cat", "dog", "elephant", "bat"]
length_group = {}

for word in words:
    length_group.setdefault(len(word), []).append(word)

print(length_group)
