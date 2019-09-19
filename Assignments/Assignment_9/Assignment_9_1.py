with open("test.txt", "r") as file:
    for line in file:
        line = line.strip().replace(" ", "")
        print(line, end="")