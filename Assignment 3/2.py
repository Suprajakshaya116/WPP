# 2. Is Fibo
# You are given a integer, N. Write a program to determine if N is an element of the Fibonacci
# Sequence.
def fibo(n):
    a,sum,b=0,0,1
    while True:
        a,b=b,sum
        if(n==sum):
            result=1
            break
        elif (sum>n):
            result=0
            break
        sum=a+b
    return result
  
t=int(input('Enter num of test cases:'))
p=[]
for i in range (t):
    a=int(input(f"Enter num {i+1}="))
    p.append(fibo(a))
for i in ("IsFibo" if j == 1 else "IsNotFibo" for j in p):
    print(i)  