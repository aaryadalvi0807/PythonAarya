words = ["  Python ", " AI ", "Machine ", " Data "]

result = [
    word.strip().lower()
    for word in words
    if len(word.strip()) > 5
]

print(result)
