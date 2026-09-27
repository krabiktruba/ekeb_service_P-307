import unittest
from ekeb_service import Course, IntensiveCourse


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

class Testing5(unittest.TestCase):
    # Stage 5!
    def test_isfull(self):
        course = Course("Колобок", 6)
        course.enrolled = 6
        self.assertTrue(course.is_full())

    def test_isfull_partly(self):
        course = Course("Колобок", 6)
        course.enrolled = 3
        self.assertEqual(course.is_full(), False)

    def test_isfull_empty(self):
        course = Course("Колобок", 6)
        self.assertEqual(course.is_full(), False)

class Testing6(unittest.TestCase):
    # Stage 6!
    def test_instance(self):
        course = IntensiveCourse("Колобок", 6, 14)
        self.assertIsInstance(course, IntensiveCourse)

    def test_workload_level_boundary_value_6(self):
        course = IntensiveCourse("Колобок", 6, 6)
        self.assertEqual(course.workload_level(), "Средняя")

    def test_workload_level_boundary_value_10(self):
        course = IntensiveCourse("Колобок", 6, 10)
        self.assertEqual(course.workload_level(), "Средняя")

    def test_workload_level_boundary_value_11(self):
        course = IntensiveCourse("Колобок", 6, 11)
        self.assertEqual(course.workload_level(), "Высокая")

    def test_workload_level_boundary_value_20(self):
        course = IntensiveCourse("Колобок", 6, 20)
        self.assertEqual(course.workload_level(), "Высокая")

    def test_workload_level_out_of_range_5(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Колобок", 6, 5)

    def test_workload_level_out_of_range_21(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Колобок", 6, 21)