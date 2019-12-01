n = int(input("Enter an integer(>=0)"))
bin_str = ""

if n == 0:
    bin_str = "0"
else:
    while n != 0:
        bin_str += str(n%2)
        n //= 2

print(bin_str[::-1])