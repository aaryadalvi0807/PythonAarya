def check_odd_even(start, end):


    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Example usage
check_odd_even(1, 10)
