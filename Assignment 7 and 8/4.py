# 4. Create a class "Employee" with attributes name and salary. Implement overloaded operators +
# and - to combine and compare employees based on their salaries.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        combined_salary = self.salary + other.salary
        combined_name = self.name + " & " + other.name
        return Employee(combined_name, combined_salary)

    def __sub__(self, other):
        salary_difference = abs(self.salary - other.salary)
        return salary_difference

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp3 = emp1 + emp2
print(emp3)   
 
print(emp1 < emp2)   
print(emp1 <= emp2) 
print(emp1 > emp2)  
print(emp1 >= emp2) 
print(emp1 == emp2)  
print(emp1 != emp2) 

# Salary difference
print(emp1 - emp2)  # 10000
