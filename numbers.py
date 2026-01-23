n = int(input("Enter a number: "))

even_numbers = []
odd_numbers = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers list:", even_numbers)
print("Odd numbers list:", odd_numbers)
