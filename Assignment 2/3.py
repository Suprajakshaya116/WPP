# 3. Find Digits
# You are given a number N, you need to print the number of positions where digits exactly
# divides N.
t=int(input("Enter num of test cases:"))
print("Enter your numbers")
p=[]
for i in range (t):
    a=int(input(f"Enter num {i+1}:"))
    l=a
    count=0
    while(a>0):
        r=a%10
        if(l%r==0):
            count+=1
        a=a//10
    p.append(count)
for x in p:
    print(x)