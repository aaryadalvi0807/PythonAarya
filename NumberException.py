def main():
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        
        result = num1 / num2
        print("Result:", result)
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Please enter valid numbers")

main()