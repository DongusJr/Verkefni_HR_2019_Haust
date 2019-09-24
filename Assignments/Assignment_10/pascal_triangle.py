def make_new_row(new_row):
    triangle = []
    if new_row == []:
        return [1]
    elif new_row == [1]:
        return [1,1]
    else:
        triangle.append(1)
        for i in range(len(new_row) - 1):
            triangle.append(new_row[i] + new_row[i+1])
        triangle.append(1)
    return triangle

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
