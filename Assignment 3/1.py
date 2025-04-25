# 1. The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
# Add up the digits of that to get another new number. Keep doing this until you get a number
# that has only one digit. That number is the digital root.
n=int(input("Enter the number:"))
x=n
def digitalroot(n):
    sum=0
    if(len(str(n))==1):
        return n
    else:
        while(n!=0):
            r=n%10
            sum+=r
            n=n//10
        return digitalroot(sum)
print(f"The digital root of {x}={digitalroot(n)}")
