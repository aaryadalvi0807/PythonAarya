# Ask user for input (letters without spaces)
letters = input("Enter letters without spaces: ")

vowels = []
consonants = []

vowel_set = "aeiouAEIOU"

for ch in letters:
    if ch.isalpha():          # check if it's a letter
        if ch in vowel_set:
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels list:", vowels)
print("Consonants list:", consonants)
