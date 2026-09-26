import unittest
from ekeb_service import Student

class Testing(unittest.TestCase):
    def test_name_and_capacity_check(self):
        student = Student("Колобок", 6)
        self.assertTrue(not student.name.isdigit())
        self.assertTrue(hasattr(student, "capacity"))

    def test_enrolled(self):
        student = Student("Колобок", 6)
        self.assertEqual(student.enrolled, 0)

    def test_name(self):
        with self.assertRaises(ValueError):
            Student("", 6)

    def test_capacity_0(self):
        with self.assertRaises(ValueError):
            Student("Колобок", 0)

    def test_capacity_minus(self):
        with self.assertRaises(ValueError):
            Student("Колобок", -1)