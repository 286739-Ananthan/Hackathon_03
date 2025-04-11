"""
test_employee_manager.py
Unit tests for the EmployeeManager class.
"""

import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    """Test cases for managing employee operations."""

    def setUp(self):
        """
        Set up test environment by initializing EmployeeManager
        and adding a test employee.
        """
        self.manager = EmployeeManager()
        self.test_emp = self.manager.add_employee(
            "Anoop", "Finance", "Analyst", 15000, 2000, 1000
        )

    def test_add_employee(self):
        """
        Test adding a new employee and check if it exists in the manager.
        """
        emp = self.test_emp
        self.assertIn(emp, self.manager.view_all())

    def test_find_by_id_valid(self):
        """
        Test searching for an employee by valid ID.
        """
        emp = self.manager.find_by_id(self.test_emp.id)
        self.assertIsNotNone(emp)
        self.assertEqual(emp.name, "Anoop")

    def test_find_by_id_invalid(self):
        """
        Test searching for an employee with an invalid ID.
        """
        emp = self.manager.find_by_id(999)
        self.assertIsNone(emp)

    def test_delete_employee_success(self):
        """
        Test successful deletion of an existing employee.
        """
        deleted = self.manager.delete_employee(self.test_emp.id)
        self.assertTrue(deleted)
        self.assertIsNone(self.manager.find_by_id(self.test_emp.id))

    def test_delete_employee_failure(self):
        """
        Test deletion with an invalid/non-existent employee ID.
        """
        deleted = self.manager.delete_employee(999)
        self.assertFalse(deleted)

if __name__ == "__main__":
    unittest.main()
