max_len = 0
max_line = ""
with open("words.txt", "r") as file:
    for line in file:
        line = line.strip()
        temp_len = len(line)
        if temp_len > max_len:
            max_len = temp_len
            max_line = line
print("Longest word is '{}' of length {}".format(max_line, max_len))
        