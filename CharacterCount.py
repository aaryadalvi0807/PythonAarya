s = "apple"
char_count = {}

for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1

print(char_count)
