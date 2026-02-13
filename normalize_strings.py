# normalize_strings.py
# Normalize strings and filter by length > 5

strings = [
    "  HelloWorld  ",
    "Python",
    "  AI  ",
    "Data Science  ",
    "  Code ",
    "MachineLearning"
]

result = []

for s in strings:
    normalized = s.strip().lower()   # trim + lowercase
    if len(normalized) > 5:
        result.append(normalized)

print("Filtered Strings:", result)
