from utils import input_employee_data, print_employee_table, find_employee_index

MAX_EMPLOYEES = 8

def add_employee(employees):
    if len(employees) >= MAX_EMPLOYEES:
        print(f"Error: Cannot add more than {MAX_EMPLOYEES} employees.")
        return

    emp_id, name, department, role, salary = input_employee_data()

    # Check for duplicate ID
    for emp in employees:
        if emp['ID'] == emp_id:
            print("Error: Employee ID already exists.")
            return

    employee = {
        'ID': emp_id,
        'Name': name,
        'Department': department,
        'Role': role,
        'Salary': salary
    }
    employees.append(employee)
    print("Employee added successfully.")

def view_employees(employees):
    if not employees:
        print("No employees to display.")
        return
    print_employee_table(employees)

def search_employee(employees):
    if not employees:
        print("No employees to search.")
        return
    search_key = input("Search by ID or Name: ").strip()
    found = [emp for emp in employees if emp['ID'] == search_key or emp['Name'].lower() == search_key.lower()]
    if not found:
        print("No matching employee found.")
    else:
        print_employee_table(found)

def update_employee(employees):
    if not employees:
        print("No employees to update.")
        return
    emp_id = input("Enter Employee ID to update: ").strip()
    idx = find_employee_index(employees, emp_id)
    if idx == -1:
        print("Employee not found.")
        return

    print("What do you want to update?")
    print("1. Department")
    print("2. Role")
    print("3. Salary")
    choice = input("Enter choice (1-3): ").strip()

    if choice == '1':
        new_dept = input("Enter new Department: ").strip()
        employees[idx]['Department'] = new_dept
    elif choice == '2':
        new_role = input("Enter new Role: ").strip()
        employees[idx]['Role'] = new_role
    elif choice == '3':
        while True:
            try:
                new_salary = float(input("Enter new Salary: ").strip())
                employees[idx]['Salary'] = new_salary
                break
            except ValueError:
                print("Invalid salary. Please enter a number.")
    else:
        print("Invalid choice.")
        return
    print("Employee updated successfully.")

def delete_employee(employees):
    if not employees:
        print("No employees to delete.")
        return
    emp_id = input("Enter Employee ID to delete: ").strip()
    idx = find_employee_index(employees, emp_id)
    if idx == -1:
        print("Employee not found.")
    else:
        employees.pop(idx)
        print("Employee deleted successfully.")
