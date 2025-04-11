"""
main.py
Entry point for the Employee Management CLI application.
"""

from employee_manager import EmployeeManager
from storage import save_to_file, load_from_file

def main():
    """
    Main function that runs the CLI loop for employee management.
    """
    manager = EmployeeManager()
    employees = load_from_file()
    manager.set_employees(employees)

    while True:
        print("\n=== Employee Management CLI ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Save and Exit")
        print("6. Exit without Saving")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            dept = input("Enter department: ")
            desig = input("Enter designation: ")
            gross = float(input("Enter gross salary: "))
            tax = float(input("Enter tax amount: "))
            bonus = float(input("Enter bonus: "))
            emp = manager.add_employee(name, dept, desig, gross, tax, bonus)
            print(f"Added: {emp}")

        elif choice == '2':
            all_emps = manager.view_all()
            if all_emps:
                for emp in all_emps:
                    print(emp)
            else:
                print("No employees to display.")

        elif choice == '3':
            try:
                emp_id = int(input("Enter employee ID to search: "))
                emp = manager.find_by_id(emp_id)
                print(emp if emp else "Employee not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == '4':
            try:
                emp_id = int(input("Enter employee ID to delete: "))
                success = manager.delete_employee(emp_id)
                print("Employee deleted." if success else "Employee not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == '5':
            save_to_file(manager.view_all())
            print("Data saved. Exiting...")
            break

        elif choice == '6':
            print("Exiting without saving...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
