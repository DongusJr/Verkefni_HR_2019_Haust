def get_file_obj(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("The file {} does not exist".format(file_name))

def make_grade_list(file_obj):
    grade_list = []
    for line in file_obj:
        total_grade = 0
        first_item = True
        line = line.strip().split(",")
        if line.pop() != "l":
            for item in line:
                if first_item:
                    grade_ratio = float(item)
                    first_item = False
                else:
                    total_grade += float(item)
            grade_list.append((grade_ratio, (total_grade/(len(line)-1))))
        else:
            final_ratio = line[0]
    return grade_list, final_ratio



def calc_final_grade(grade_list, final_ratio, wanted_grade):
    now_grade = 0
    for ratio, grade in grade_list:
        now_grade += ratio*grade
    return (wanted_grade-now_grade)/float(final_ratio)

def main():
    file_name = input("What file do you want to open? ")
    file_obj = get_file_obj(file_name)
    wanted_grade = float(input("What grade do you want?"))
    
    if file_obj:
        grade_list, final_ratio = make_grade_list(file_obj)
        print(calc_final_grade(grade_list, final_ratio, wanted_grade))
        file_obj.close()

main()