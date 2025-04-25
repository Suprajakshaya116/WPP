# To do this, he follow 2 rules:
# (a) He can reduce the value of a letter. E.g. He can change ‘d’ to ‘c’ but he cannot change ‘c’ to
# ‘d’.
# (b) In order to form a palindrome, if he has to repeatedly reduce the value of a letters, he can do it
# until the letters becomes ‘a’. Once a letters has been changed to ‘a’, it can no longer be changed.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number
# of operations required to convert a given string into a palindrome.

def palin(str):
    n= int(len(str)/2)
    l=len(str)
    count=0
    #if its not palindrome,eg:"abc"->'c' is greater than a by two positions,so it will be changed twice
    # if str is"cba"->a is not grater than c so string remains unchanged
    for i in range(n):
           if(ord(str[l-(i+1)])>ord(str[(i)])):
                count+=(ord(str[l-(i+1)]))-(ord(str[(i)]))
    return count

t=int(input("no. of cases:"))
l=[]
for i in range(t):
    a=input("enter string:")
    l.append(palin(a))
for i in l:print(i)
 