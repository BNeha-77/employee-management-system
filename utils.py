def get_choice(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt).strip())
            if choice < min_val or choice > max_val:
                print(f"Please enter a number between {min_val} and {max_val}.")
            else:
                return choice
        except ValueError:
            print("Invalid input! Enter a number.")

def input_employee_data():
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    role = input("Enter Role: ").strip()
    while True:
        try:
            salary = float(input("Enter Salary: ").strip())
            break
        except ValueError:
            print("Invalid salary. Please enter a number.")
    return emp_id, name, department, role, salary

def print_employee_table(employees):
    print("\n{:<10} {:<20} {:<20} {:<20} {:<10}".format('ID', 'Name', 'Department', 'Role', 'Salary'))
    print("-" * 80)
    for emp in employees:
        print("{:<10} {:<20} {:<20} {:<20} {:.2f}".format(
            emp['ID'], emp['Name'], emp['Department'], emp['Role'], emp['Salary']
        ))
    print("-" * 80)

def find_employee_index(employees, emp_id):
    for i, emp in enumerate(employees):
        if emp['ID'] == emp_id:
            return i
    return -1
