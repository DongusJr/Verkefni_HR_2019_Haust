from operator import itemgetter

my_dic = {"dongo": 1, "bongus": 2, "flingus": 3}

print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())
print("Sorted: ")
print(sorted(my_dic.keys()))
print(sorted(my_dic.values()))
print(sorted(my_dic.items()))

print(sorted(my_dic.items(), key=itemgetter(1), reverse=False))