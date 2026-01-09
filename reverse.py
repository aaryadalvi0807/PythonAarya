# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

# Function to take input from user
def get_number():
    return int(input("Enter a number: "))

# Function to display the result
def display_result(original, reversed_num):
    print(f"Original number: {original}")
    print(f"Reversed number: {reversed_num}")

# Main function
def main():
    number = get_number()
    reversed_num = reverse_number(number)
    display_result(number, reversed_num)

# Run the program
if __name__ == "__main__":
    main()
