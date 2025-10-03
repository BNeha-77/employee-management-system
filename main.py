from employee_functions import add_employee, view_employees, search_employee, update_employee, delete_employee
from utils import get_choice

def menu():
    employees = []
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = get_choice("Enter your choice: ", 1, 6)

        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            view_employees(employees)
        elif choice == 3:
            search_employee(employees)
        elif choice == 4:
            update_employee(employees)
        elif choice == 5:
            delete_employee(employees)
        elif choice == 6:
            print("Exiting Employee Management System. Goodbye!")
            break

if __name__ == "__main__":
    menu()
