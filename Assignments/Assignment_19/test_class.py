print("-------WholeNUMBER-------")
from whole_number import WholeNumber
from student import Student

num1 = WholeNumber(1)
print(num1)

num1 = WholeNumber(3)
num2 = WholeNumber(4)
num3 = num1 + num2
print(num3)

num2 = WholeNumber(2)
num3 = num1 * num2
print(num3)

num3 = num1 - num3
print(num3)

print("-------Student-------")
student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
student2 = Student(2, [9.5, 9.0, 8.9, 9.8])

print(student1)
if student1 < student2:
    print("student1 < student2")

# print("-------Account-------")

# def print_accounts(accounts):
#     for account in accounts:
#         print(account)

# def update_accounts(accounts):
#     for account in accounts:
#         account.update_account()


# from account import SavingsAccount, DebitAccount

# s1 = SavingsAccount(1000)
# d1 = DebitAccount(1000)
# s2 = SavingsAccount(2000)
# d2 = DebitAccount(4000)

# accounts = [s1,d1,s2,d2]
# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

print("------Employee-------")
from employee import HourlyEmployee, SalariedEmployee, Manager

def print_salaries(staff):
    for employee in staff:
        name = employee.get_name()
        hours = int(input("Hours worked by " + name + ": "))
        pay = employee.weekly_pay(hours)
        print("{}: {:.2f}".format(name, pay))

# The main program starts here
staff = []
staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
staff.append(SalariedEmployee("Sally Lin", 52000.0)) # 52000 is the annual salary
staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
print_salaries(staff)