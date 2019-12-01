def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("File not found!")
        return None

def make_sales_list(file_obj):
    sales_list = []
    for line in file_obj:
        sales = [int(i) for i in line.strip().split(" ")]
        sales_list.append(sales)
    return sales_list

def calc_average(sales_list):
    average_dict = {}
    for i, sales in enumerate(sales_list):
        average = (sum(sales)/len(sales))
        average_dict[i+1] = average
    return average_dict

def print_results(average_dict):
    print("Average sales:")
    for number, average in sorted(average_dict.items()):
        print("Department no. {}: {:.1f}".format(number, average))

def main():
    file_name = input("Enter file name: ")
    file_obj = open_file(file_name)
    if file_obj:
        sales_list = make_sales_list(file_obj)
        average_dict = calc_average(sales_list)
        print_results(average_dict)
main()