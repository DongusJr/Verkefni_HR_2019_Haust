n = int(input("Enter height of the triangle: "))

def make_new_row(old_row):
    if len(old_row) < 2:
        old_row += [1]
        return old_row
    else:
        new_row = [old_row[0]]
        for i in range(len(old_row) - 1):
            new_row.append(old_row[i]+old_row[i+1])
        new_row.append(old_row[-1])
        return new_row


new_row = []
for i in range(1, n+1):
    new_row = make_new_row(new_row)
    print(new_row)