# 6. Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula]
l=[]
n=3
for i in range (n):
    a=list((input(f"enter point {i+1}:")).split(","))
    l.append(a)
for i in range(n):
    for j in range(3):
        l[i][j]=int(l[i][j])
 
d={}
for i in l:
    a=10000
    for j in l:
        if(j!=i):
            d=(( i[0]-j[0] )**2) +(( i[1]- j[1])**2) +((i[2]-j[2])**2)
            if a>d:
                a=d
                closest=j
    print(f"{i} is close to :{closest}",end="\n")
     
 
 