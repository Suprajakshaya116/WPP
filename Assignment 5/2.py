'''
2. Halloween Party
Alex is attending a Halloween party with his girlfriend Silvia. At the party, Silvia spots a giant
chocolate bar. If the chocolate can be served as only 1*1 sized pieces and Alex can cut the
chocolate bar exactly K times, what is the maximum number of chocolate pieces Alex can cut and
give Silvia?
For the first test-case where K=5, You need 3 Horizontal and 2 Vertical cuts.n=2*3=6->max number of chocolate pieces
For the second test case where K=6, You need 3 Horizontal and 3 Vertical cuts.n=3*3=9->max number of chocolate pieces
'''
t=int(input())
l=[]
k=list(map(int,input().split()))
for i in range(0,t): 
    if k[i]%2==0:
        n=k[i]/2
        l.append(n**2)
    else:
        n=k[i]//2
        l.append(n*(n+1))
for i in l:
    print(int(i))