class Student:
    def __init__(self, name, capacity):
        if not name:
            raise ValueError("Имя студента не может быть пустым.")
        if capacity < 1:
            raise ValueError("Количество не может быть отрицательным.")
        self.name = name
        self.capacity = capacity
        self.enrolled = 0