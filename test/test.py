from itertools import permutations

NUMBERS = int(input("yo hversu langt? "))
yule_lads = [int(i+1) for i in range(NUMBERS)]
count = 0
perm = permutations(yule_lads)
found_seqs = []
number_count = 0
for sequence in list(perm):
    number_count = 0
    for index, number in enumerate(sequence):
        if yule_lads[index] != number:
            number_count += 1
        if number_count == NUMBERS:
            count += 1
            found_seqs.append(sequence)

print("Count: {}".format(count))
print("Sequences valid:")
for seq in found_seqs:
    print(seq)
