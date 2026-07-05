import csv
import json

# Person Class
class Person:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

# Employee Class
class Employee(Person):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

# Manager Class
class Manager(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

# File Handler Class
class FileHandler:

    def read_csv(self, filename):
        employees = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
        return employees

    def read_json(self, filename):
        with open(filename, "r") as file:
            return json.load(file)

# Report Generator Class
class ReportGenerator:

    def generate_summary(self, employees):
        for emp in employees:
            salary = emp.calculate_salary()

            if salary > 50000:
                status = "High Income"
            else:
                status = "Normal"

            print(emp.name, salary, status)

# Main Program
file = FileHandler()

employee_data = file.read_csv("employees.csv")
bonus_data = file.read_json("bonus.json")

employees = []

for row in employee_data:
    emp_id = row["id"].strip()
    name = row["name"].strip()
    salary = int(row["salary"])

    # Create Manager only for Kiran
    if name == "Kiran":
        bonus = 10000
        emp = Manager(name, emp_id, salary, bonus)
    else:
        emp = Employee(name, emp_id, salary)

    employees.append(emp)

report = ReportGenerator()
report.generate_summary(employees)