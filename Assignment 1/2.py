# 2. Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random
 
random_list = [random.randint(0, 1) for _ in range(100)]

print(random_list)

count=0;max_zeroes=0

for i in random_list:
    if(i==0):
        count+=1
    else:
        max_zeroes=max(count,max_zeroes)
        count=0

print(max_zeroes)

    