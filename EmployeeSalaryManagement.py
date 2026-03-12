# Base Class
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Base Salary:", self.base_salary)

    def annual_salary(self):
        return self.base_salary * 12


# Derived Class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, department, bonus):
        super().__init__(emp_id, name, base_salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self):
        return self.annual_salary() + self.bonus

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)
        print("Bonus:", self.bonus)
        print("Total Annual Salary:", self.total_salary())
        print("------------------------")


# Creating Manager objects
m1 = Manager(101, "Rahul", 50000, "IT", 100000)
m2 = Manager(102, "Anita", 60000, "HR", 80000)
m3 = Manager(103, "Vikas", 55000, "Finance", 90000)

# Storing in a list
managers = [m1, m2, m3]

# Display all managers
for m in managers:
    m.display_manager()