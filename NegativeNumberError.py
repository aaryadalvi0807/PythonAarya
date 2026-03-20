class NegativeNumberError(Exception):
    pass

def main():
    try:
        num = int(input("Enter a number: "))
        
        if num < 0:
            raise NegativeNumberError("Negative numbers are not allowed!")
        
        print("You entered:", num)

    except NegativeNumberError as e:
        print("Error:", e)

    except ValueError:
        print("Error: Please enter a valid integer")

if __name__ == "__main__":
    main()
    
