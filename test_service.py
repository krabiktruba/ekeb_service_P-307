# Практическая номер 2
import unittest
from service import print_cost, exam_result, Student, GrantStudent


class TestingA1(unittest.TestCase):
    # print_cost
    def test_0_pages(self):
        self.assertEqual(print_cost(0), 0)

    def test_1_page(self):
        self.assertEqual(print_cost(1), 30)

    def test_9_pages(self):
        self.assertEqual(print_cost(9), 270)

    def test_10_pages(self):
        self.assertEqual(print_cost(10), 270)

    def test_11_pages(self):
        self.assertEqual(print_cost(11), 297)

    def test_negative(self):
        with self.assertRaises(ValueError):
            print_cost(-2)

    # exam_result
    def test_exam_overscore(self):
        with self.assertRaises(ValueError):
            exam_result(101)

    def test_exam_negative(self):
        with self.assertRaises(ValueError):
            exam_result(-1)

    def test_0(self):
        self.assertEqual(exam_result(0), "Незачёт")

    def test_49(self):
        self.assertEqual(exam_result(49), "Незачёт")

    def test_50(self):
        self.assertEqual(exam_result(50), "Зачёт")

    def test_51(self):
        self.assertEqual(exam_result(51), "Зачёт")

    def test_100(self):
        self.assertEqual(exam_result(100), "Зачёт")


class TestingA3(unittest.TestCase):
    def setUp(self):
        self.student = Student("Алия", 50)

    def test_class_attribute_name(self):
        self.assertTrue(hasattr(self.student, "name"))

    def test_class_attribute_score(self):
        self.assertTrue(hasattr(self.student, "score"))

    def test_has_passed_49(self):
        self.student.score = 49
        self.assertEqual(self.student.has_passed(), False)

    def test_has_passed_50(self):
        self.student.score = 50
        self.assertEqual(self.student.has_passed(), False)

    def test_has_passed_51(self):
        self.student.score = 51
        self.assertEqual(self.student.has_passed(), True)

    def test_add_points(self):
        self.student.add_points(10)
        self.assertEqual(self.student.score, 60)

    def test_add_points_maximum(self):
        self.student.add_points(51)
        self.assertEqual(self.student.score, 100)

    def test_points_negative(self):
        with self.assertRaises(ValueError):
            self.student.add_points(-51)

class TestingA4(unittest.TestCase):
    def test_class_instance(self):
        student = GrantStudent("Не Алия", 50)
        self.assertIsInstance(student, GrantStudent)

    def test_class_instancing(self):
        student = GrantStudent("Не Алия", 50)
        self.assertTrue(student.add_points(10), student.score == 60)
        print(student.grant_status())