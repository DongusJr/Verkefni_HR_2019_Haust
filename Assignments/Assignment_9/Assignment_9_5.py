file_input = input("Enter filename: ")
read_file = open(file_input, "r")
write_file = open("sentences.txt", "w")
first_word = True

for line in read_file:
    line = line.strip()
    if line == "":
        continue
    elif first_word:
        print(line, end="")
        print(line, end="", file=write_file)
        first_word = False
    elif line == ".":
        print(".")
        print(".", file=write_file)
        first_word = True
        continue
    elif line == ",":
        print(",", end="")
        print(",", end="", file=write_file)
    else:
        print(" ", end="")
        print(line, end="")
        print(" ", end="", file=write_file)
        print(line, end="", file=write_file)
        
read_file.close()
write_file.close()