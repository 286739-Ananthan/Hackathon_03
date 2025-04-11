"""
employee.py
Defines the Employee class and encapsulates salary calculations.
"""

class Employee:
    # Class-level ID counter to auto-generate unique IDs
    id_counter = 1

    def __init__(self, name, department, designation, gross_salary, tax, bonus):
        """
        Initialize an Employee instance.
        
        Args:
            name (str): Employee's name.
            department (str): Department name.
            designation (str): Employee's job title.
            gross_salary (float): Total salary before deductions.
            tax (float): Tax amount to deduct.
            bonus (float): Additional bonus to add.
        """
        self.id = Employee.id_counter
        Employee.id_counter += 1
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        """
        Calculate net salary after applying tax and bonus.
        
        Returns:
            float: Net salary.
        """
        return self.gross_salary - self.tax + self.bonus

    def __str__(self):
        """
        Return a string representation of the employee.
        
        Returns:
            str: Employee details in readable format.
        """
        return (f"ID: {self.id}, Name: {self.name}, Department: {self.department}, "
                f"Designation: {self.designation}, Net Salary: {self.net_salary}")