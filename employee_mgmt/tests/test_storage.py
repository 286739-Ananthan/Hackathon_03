"""
test_storage.py
Unit tests for file-based storage using Pickle.
"""

import unittest
import os
from employee import Employee
from storage import save_to_file, load_from_file

class TestStorage(unittest.TestCase):
    """Test cases for saving and loading employee data to/from file."""

    def setUp(self):
        """
        Set up by creating a sample employee and a temporary file path.
        """
        self.test_emp = Employee("David", "Sales", "Rep", 8000, 800, 200)
        self.test_file = "test_employees.pkl"

    def test_save_and_load_employees(self):
        """
        Test saving a list of employees and loading them back.
        """
        save_to_file([self.test_emp], self.test_file)
        loaded = load_from_file(self.test_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "David")

    def tearDown(self):
        """
        Clean up by deleting the test file after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
