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


class Testing3(unittest.TestCase):
    # Stage 3!
    def test_enroll(self):
        course = Course("Колобок", 6)
        self.assertEqual(course.enroll(), 1)

    def test_enroll_serial_registration(self):
        course = Course("Колобок", 6)
        course.enroll()
        course.enroll()
        course.enroll()
        course.enroll()
        self.assertEqual(course.enrolled, 4)

    def test_enroll_last_place(self):
        course = Course("Колобок", 6)
        course.enrolled = 5
        course.enroll()
        self.assertEqual(course.enrolled, 6)

    def test_enroll_overcharge(self):
        course = Course("Колобок", 6)
        course.enrolled = 6
        with self.assertRaises(ValueError):
            course.enroll()

class Testing4(unittest.TestCase):
    # Stage 4!
    def test_cancel_enrollment(self):
        course = Course("Колобок", 6)
        course.enrolled = 1
        course.cancel_enrollment()
        self.assertEqual(course.enrolled, 0)

    def test_cancel_enrollment_overcancelling(self):
        course = Course("Колобок", 6)
        with self.assertRaises(ValueError):
            course.cancel_enrollment()

    def test_cancel_enrollment_regeneration(self):
        course = Course("Колобок", 6)
        course.enrolled = 1
        course.cancel_enrollment()
        course.enroll()
        self.assertEqual(course.enrolled, 1)