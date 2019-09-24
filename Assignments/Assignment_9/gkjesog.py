
fac_40 = 1
fac_20 = 1
for i in range(1, 41):
    fac_40 *= i
for i in range(1, 21):
    fac_20 *= i

print((fac_40/fac_20)/fac_20)

big_number = 2**1000
sum_num = 0
while(big_number!=0):
    sum_num += big_number%10
    big_number //= 10

print(sum_num)