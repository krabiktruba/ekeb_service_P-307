class Course:
    def __init__(self, name, capacity):
        if not name:
            raise ValueError("Имя студента не может быть пустым.")
        if capacity < 1:
            raise ValueError("Количество не может быть отрицательным.")
        self.name = name
        self.capacity = capacity
        self.enrolled = 0

    def available_places(self):
        return self.capacity - self.enrolled

    def enroll(self):
        self.enrolled += 1
        if self.enrolled > self.capacity:
            raise ValueError("Места закончились.")
        return self.enrolled