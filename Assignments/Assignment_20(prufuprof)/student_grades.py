def get_input_dict():
    ''' Function that takes input from the user and makes a dictionary with name and grade of student '''
    name_dict = {}
    for i in range(4):  # 4 Names
        student_name = input("Student name: ")
        for j in range(3):  # 3 grades per student
            grade_number = float(input("Input grade number {}: ".format(j+1)))
            if student_name in name_dict:  # If the student is already in the dict
                name_dict[student_name].append(grade_number)
            else:  # If he is not in the dict, initialize a list with the grades
                name_dict[student_name] = [grade_number]
    return name_dict
        

def get_highest_average(grade_dict):
    ''' Function that calculates which student has the highest
        average grade and returns that info in a tuple '''
    max_name = ""  # Name of the highest average
    max_grade = 0
    for name, grades in sorted(grade_dict.items()):
        average_grade = (sum(grades)/len(grades))  # Take the average grade for each student
        if average_grade == max_grade:  # If the max_grade is equal to the students grade, check their name alphabetically
            if name[0] < max_name[0]:  # If the name is earlier in the alphabet
                max_name = name
        elif average_grade > max_grade:  # Else if the students grade is higher, then safe it
            max_grade = average_grade
            max_name = name
    return (max_name, max_grade)  # return as a tuple


def print_output(grade_dict, max_tuple):
    ''' Function that prints out the output '''
    print("Student list:")
    for name, grades in sorted(grade_dict.items()):
        print("{}: {}".format(name, str(grades)))
    print("Student with highest average grade:")
    print("{} has an average grade of {:.2f}".format(max_tuple[0], max_tuple[1]))

def main():
    ''' Main function of this program '''
    grade_dict = get_input_dict()
    max_tuple = get_highest_average(grade_dict)
    print_output(grade_dict, max_tuple)


main()