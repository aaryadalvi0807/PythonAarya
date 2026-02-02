words = ["python", "java", "python", "c", "java"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

result = {k: v for k, v in freq.items() if v > 1}
print(result)
