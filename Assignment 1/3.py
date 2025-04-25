# 3. Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.
l=int(input('Enter the length in feet: '))
print("Enter your option for conversion")
list=['inches','yards','miles','millimeters','centimeters','meters','kilometers']
for i,j in enumerate(list):
    print(i,':',j)
a=int(input())
b=[l*12,l*0.333,l*0.0001893,l*304.8,l*30.48,l*0.3048,l*0.0003048]
print(l,'feet =',b[a],list[a])