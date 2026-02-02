s = "banana"
index_map = {}

for i, ch in enumerate(s):
    index_map.setdefault(ch, []).append(i)

# convert lists to tuples
index_map = {k: tuple(v) for k, v in index_map.items()}

print(index_map)
