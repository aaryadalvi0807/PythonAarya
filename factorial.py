# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to get input from the user
def get_number():
    return int(input("Enter a number: "))

# Function to display the result
def display_result(number, fact):
    print(f"Factorial of {number} is {fact}")

# Main function
def main():
    number = get_number()
    fact = factorial(number)
    display_result(number, fact)

# Run the program
if __name__ == "__main__":
    main()
