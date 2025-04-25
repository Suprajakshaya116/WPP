# 5. Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).
import numpy as np

print("Enter list of strings seperted by commas(',')")
l=list(input().split(','))

def formating_strings(l):
    arr=np.array([s[:15] for s in l])
    left_justify=np.char.ljust(arr,15,'_')
    right_justify=np.char.rjust(arr,15,'_')
    centered=np.char.center(arr,15,'_')
    return left_justify,right_justify,centered

left,right,centered=formating_strings(l)
print(f"\nleft justified:{left}\n",f"right justified:{right}\n",f"centered:{centered}\n",sep='\n')
 