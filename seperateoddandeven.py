# Function to separate odd and even numbers
def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return odd_numbers, even_numbers

# Function to take input from user
def get_numbers():
    nums = input("Enter numbers separated by spaces: ").split()
    return [int(num) for num in nums]

# Function to display the results
def display_results(odd_numbers, even_numbers):
    print("Odd numbers:", odd_numbers)
    print("Even numbers:", even_numbers)

# Main function
def main():
    numbers = get_numbers()
    odd_numbers, even_numbers = separate_odd_even(numbers)
    display_results(odd_numbers, even_numbers)

# Run the program
if __name__ == "__main__":
    main()

