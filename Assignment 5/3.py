def next_lexicographical(s):
    i=len(s)-1 #starts from last index
    s=list(c for c in s)
    while i>0 : 
        if(s[i]>s[i-1]):#if before element is smaller
            s[i],s[i-1]=s[i-1],s[i]#swap elements
            break
        i=i-1  
    else:
        return "no answer"#if sting is in descending order , no answer

    s = s[:i] + sorted(s[i:])#from the index i position sorting the elements(so that we can get smallest string from all)  
    return ''.join(s)
t=int(input())
l=[]
for i in range(0,t):
    w=input()
    l.append(next_lexicographical(w))
for i in l:
    print(i)