# Практическая номер 2 (исправленная версия!)
def print_cost(pages):
    if pages < 0:
        raise ValueError
    total = pages * 30
    if pages >= 10:
        total = total * 0.9
    return total

def exam_result(score):
    if score < 0 or score > 100:
        raise ValueError("Недопустимый балл")
    if score >= 50:
        return "Зачёт"
    return "Незачёт"

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def has_passed(self):
        return self.score > 50

    def add_points(self, points):
        self.score += points
        if self.score > 100:
            self.score = 100
        elif self.score < 0:
            raise ValueError
        return self.score

class GrantStudent(Student):
    def __init__(self, name, score):
        super().__init__(name, score)

    def grant_status(self):
        return "Грант сохранён" if self.score >= 70 else "Грант не сохранён"

class ExcellentStudent(Student):
    def __init__(self, name, score):
        super().__init__(name, score)

    def scholarship(self):
        if self.score >= 90:
            return 30000
        elif 75 <= self.score <= 89:
            return 15000
        return 0