# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to get input from the user
def get_number():
    return int(input("Enter the value of n: "))

# Function to display prime numbers
def display_primes(n):
    print(f"Prime numbers between 1 and {n} are:")
    for num in range(1, n + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  # for new line

# Main function
def main():
    n = get_number()
    display_primes(n)

# Run the program
if __name__ == "__main__":
    main()
