# 3. Utopian Tree
# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
# monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
# increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
# the height of the tree after N growth cycles?
def tree(n):  
    sum=1
    if n==0:
        return 1
    for i in range(1,n+1):
        if i%2==0:
            sum+=1
        else: 
            sum*=2
    return sum
l=[]
t=int(input("enter num of test cases: "))
for i in range(t):
    a=int(input("enter num of cycles:"))
    l.append(tree(a))   
for i in l:
    print(i)