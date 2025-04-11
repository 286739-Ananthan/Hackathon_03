from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        emp = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(emp)
        return emp

    def view_all(self):
        return self.employees

    def find_by_id(self, emp_id):
        return next((e for e in self.employees if e.id == emp_id), None)

    def delete_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        if emp:
            self.employees.remove(emp)
            return True
        return False

    def set_employees(self, employee_list):
        self.employees = employee_list
        if employee_list:
            Employee.id_counter = max(emp.id for emp in employee_list) + 1