import random
random_seed = int(input("give seed: please: please: "))
random.seed(random_seed)
print(random_seed)


test_list = [1,2,3]
random_list = []

for i in range(5):
    random_list.append(random.choice(test_list))

print(random_list)