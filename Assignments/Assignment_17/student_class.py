class Student():
    def __init__(self, score=10):
        self.score = score

    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    def __str__(self):
        return str(self.score)

p = Student()

print(p)

p.add_score()

print(p)

p.decrease_score()

print(p)