#2. count the number of square integers between A and B (both inclusive).
def square(a,b):
    i=1
    count=0
    while(True):
        val=i**2
        i+=1
        if val>b:
            break
        if val in range(a,b+1):
           count+=1 
    return count
t=int(input("no. of cases:"))
l=[]
for i in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    l.append(square(a,b))
for i in l:print(i)
 