class Employee:
    def __init__(self, name = "", wage = 0):
        self.name = name
        self.wage = wage

    def get_name(self):
        return self.name

class HourlyEmployee(Employee):
    def __init__(self, name= "", wage= 0):
        Employee.__init__(self, name, wage)

    def weekly_pay(self, hours):
        if hours <= 40:
            return self.wage * hours
        else:
            return (self.wage*40) + (self.wage * 1.5 * (hours - 40))

class SalariedEmployee(Employee):
    def __init__(self, name="", wage= 0):
        Employee.__init__(self, name, wage)
        WEEKS = 52
        self.weeks = WEEKS

    def weekly_pay(self, hours):
        return self.wage /self.weeks

class Manager(SalariedEmployee):
    def __init__(self, name="", wage=0, bonus=0):
        SalariedEmployee.__init__(self, name, wage)
        self.bonus = bonus
        
    def weekly_pay(self, hours):
        return (self.wage / self.weeks) + self.bonus

    