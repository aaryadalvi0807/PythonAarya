def get_age():
    """Get age input from the user"""
    age = int(input("Enter your age: "))
    return age


def classify_age(age):
    """Classify the age group"""
    if age < 0:
        return "Invalid age"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"


def main():
    age = get_age()
    category = classify_age(age)
    print("Category:", category)


# Program execution starts here
main()
       
    
