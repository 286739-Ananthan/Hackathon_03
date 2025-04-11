"""
test_employee.py
Unit tests for the Employee class.
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test cases for Employee salary calculation."""

    def test_net_salary_calculation(self):
        """
        Test that net salary is correctly calculated:
        net_salary = gross_salary - tax + bonus
        """
        emp = Employee("Anil", "IT", "Developer", 10000, 1000, 500)
        expected_net = 9500
        self.assertEqual(emp.net_salary, expected_net)

    def test_employee_fields(self):
        """
        Test that employee fields are correctly assigned.
        """
        emp = Employee("Kumar", "HR", "Manager", 12000, 1200, 300)
        self.assertEqual(emp.name, "Bob")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.designation, "Manager")

if __name__ == "__main__":
    unittest.main()
