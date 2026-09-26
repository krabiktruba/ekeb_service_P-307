import unittest
from ekeb_service import Course

class Testing(unittest.TestCase):
    def test_name_and_capacity_check(self):
        student = Course("Колобок", 6)
        self.assertTrue(not student.name.isdigit())
        self.assertTrue(hasattr(student, "capacity"))

    def test_enrolled(self):
        student = Course("Колобок", 6)
        self.assertEqual(student.enrolled, 0)

    def test_name(self):
        with self.assertRaises(ValueError):
            Course("", 6)

    def test_capacity_0(self):
        with self.assertRaises(ValueError):
            Course("Колобок", 0)

    def test_capacity_minus(self):
        with self.assertRaises(ValueError):
            Course("Колобок", -1)

class Testing2(unittest.TestCase):
    # Stage 2!
    def test_available_places(self):
        course = Course("Колобок", 6)
        course.enrolled = 4
        self.assertEqual(course.available_places(), 2)

