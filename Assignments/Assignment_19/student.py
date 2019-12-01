class Student:
    def __init__(self, id, grades):
        self.id = id
        self.grades = grades
    
    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.id, str(self.grades))
    
    def __lt__(self, other):
        avg_self, avg_other = 0,0
        for i in range(len(self.grades)):
            avg_self += self.grades[i]
            avg_other += other.grades[i]
        return avg_self < avg_other

