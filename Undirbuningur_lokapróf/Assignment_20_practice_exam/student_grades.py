def get_input():
    student_dict = {}
    for i in range(4):
        student_name = input("Student name: ")
        for j in range(3):
            student_grade = float(input("Input grade number {}: ".format(j+1)))
            if student_name in student_dict:
                student_dict[student_name].append(student_grade)
            else:
                student_dict[student_name] = [student_grade]
    return student_dict

def get_highest_average(student_dict):
    max_grade = 0
    max_student = ""
    for student, grades in sorted(student_dict.items()):
        average_grade = sum(grades)/len(grades)
        if average_grade > max_grade:
            max_grade = average_grade
            max_student = student
    return (max_student, max_grade)

def print_output(student_dict, max_grade_tuple):
    print("Student list: ")
    for student, grades in sorted(student_dict.items()):
        print("{}: {}".format(student, str(grades)))
    print("Student with highest average grade: ")
    print("{} has an average grade of {:.2f}".format(max_grade_tuple[0], max_grade_tuple[1]))

def main():
    student_dict = get_input()
    max_grade_tuple = get_highest_average(student_dict)
    print_output(student_dict, max_grade_tuple)
main()