'''pangrams'''
str=input()
alpha=list(map(chr,range(97,123)))
str=(sorted(str))
i=j=count=0
while i<len(alpha) and j<len(str):
    if str[j]==alpha[i]:
         i+=1
         count+=1
    j+=1
if count ==len(alpha):
     print("pangram")
else:
     print("not pangram")
 