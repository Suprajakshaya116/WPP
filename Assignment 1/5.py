# 5. You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]
def reverse(name):
    new=''
    for i in range(len(name)):
         r=name[-1]
         new+=r
         name=name[:len(name)-1]#slicing last letter 
    return new
l=[]
for i in range(3):
    a=input('enter name(less than 15 characters are allowed): ')
    l.append(a)
for i in l:
    print(reverse(i))