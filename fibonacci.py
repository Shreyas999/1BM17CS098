def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the value of n :"))
print("Fibonacci series :",)
for i in range(n):
    print(fib(i),end=" ")

'''OUTPUT:
Enter the value of n :10
Fibonacci series :
0 1 1 2 3 5 8 13 21 34 
'''
