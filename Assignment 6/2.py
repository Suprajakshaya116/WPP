# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.
# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.
'''
         
           R  p   s 
     com-> 0  1  2 
 player  0 D  L  W
         1 w  D  L
         2 L  W  D
    '''   
from random import randint  
class Rock_paper_scissors:
    count=win=lost=0
    l= [['draw','lost','won'],
        ['won','draw','lost'],
        ['lost','won','draw']] 
    option=["Rock","paper","scissor"]
    def comp(self):
        return self.option[self.computer]
    def result(self):
        print('''\nHello player
choose your option
0=Rock
1=paper
2=scissor''')
        self.computer=randint(0,2)
        p=int(input())
        self.count+=1
        if self.l[p][self.computer]=='won':
            self.win+=1
        elif self.l[p][self.computer]=='lost':
            self.lost+=1
        return f"round {self.count} result:{self.l[p][self.computer]}"
    def winner(self):
    
        if self.win>self.lost:
            print("\n***you won the game:)***")
        elif self.win<self.lost:
            print("\n***you lost!Better luck next time***")   
        else :print("***DRAW***")
c=Rock_paper_scissors()
for i in range(0,3):
    print(c.result())
    print("computer option was:"+c.comp())
c.winner()
    


    