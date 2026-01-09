# Function to count digits in a number
def count_digits(number):
    count = 0
    if number == 0:
        return 1
    while number != 0:
        number = number // 10
        count += 1
    return count

# Function to get input from the user
def get_number():
    return int(input("Enter a number: "))

# Function to display the result
def display_result(number, digit_count):
    print(f"The number {number} has {digit_count} digits.")

# Main function
def main():
    number = get_number()
    digit_count = count_digits(number)
    display_result(number, digit_count)

# Run the program
if __name__ == "__main__":
    main()
