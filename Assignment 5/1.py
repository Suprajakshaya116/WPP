# 1. Maximizing XOR
# Given two integers: L and R, Find the maximal values of A xor B given, L <= A <= B <= R
# Input Format:The input contains two lines, L is present in the first line. R in the second line.
# Constraints: 1 <= L <= R <= 10**3
def xor(a,b):
    max=0
    for i in range(a,b+1):
        for j in range(i,b+1):
            var=i^j
            if(var>max):
                max=var
    print(max )
a,b=int(input()),int(input()) 
xor(a,b)
