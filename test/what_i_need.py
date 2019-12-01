def get_file_obj(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("The file {} does not exist".format(file_name))
        return None

def get_average(file_obj):
    average = 0
    for line in file_obj:
        grades = line.strip().split(",")
        weight = grades.pop(0)
        grades = [float(i) for i in grades]
        average += float(weight)*(sum(grades)/len(grades))
    return average
        

def main():
    file_name = input("What file do you want to open? ")
    file_obj = get_file_obj(file_name)
    if file_obj:
        average = get_average(file_obj)
        print(average)

main()