# Your function definition goes here
def fibo(n):
    a_n2 = 1
    a_n1 = 1
    for i in range (1, n+1):
        if i == 1 or i == 2:
            print(1, end= " ")
        else:
            a_n = a_n1 + a_n2
            print(a_n, end= " ")
            a_n2 = a_n1
            a_n1 = a_n
        
        #a(n) = a(n-1) + a(n-2)

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
fibo(n)