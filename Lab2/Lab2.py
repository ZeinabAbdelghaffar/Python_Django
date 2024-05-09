from tabulate import tabulate

class Employee:
    employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)

    def transfer(self, new_department):
        self.department = new_department

    def fire(self):
        Employee.employees.remove(self)

    def show(self):
        data = [[self.first_name, self.last_name, self.age, self.department, self.salary, "Employee", ""]]
        headers = ["First Name", "Last Name", "Age", "Department", "Salary", "Type", "Managed Department"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    @staticmethod
    def list_employees():
        data = [[employee.first_name, employee.last_name, "Employee"] for employee in Employee.employees]
        headers = ["First Name", "Last Name", "Type"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        data = [[self.first_name, self.last_name, self.age, self.department, self.salary, "Manager", self.managed_department]]
        headers = ["First Name", "Last Name", "Age", "Department", "Salary", "Type", "Managed Department"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

def main():
    employees = []
    managers = []
    while True:
        print("1. Add Employee")
        print("2. Add Manager")
        print("3. Show Employees")
        print("4. Quit")
        choice = input("Enter your choice num: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = int(input("Enter salary: "))
            employee = Employee(first_name, last_name, age, department, salary)
            employees.append(employee)
            print("\nEmployee added successfully\n")

        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = int(input("Enter salary: "))
            managed_department = input("Enter managed department: ")
            manager = Manager(first_name, last_name, age, department, salary, managed_department)
            managers.append(manager)
            print("\nManager added successfully\n")

        elif choice == "3":
            data = []
            for employee in employees:
                data.append([employee.first_name, employee.last_name, employee.age, employee.department, employee.salary, "Employee", ""])
            for manager in managers:
                data.append([manager.first_name, manager.last_name, manager.age, manager.department, manager.salary, "Manager", manager.managed_department])
            headers = ["First Name", "Last Name", "Age", "Department", "Salary", "Type", "Managed Department"]
            print(tabulate(data, headers=headers, tablefmt="grid"))

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
