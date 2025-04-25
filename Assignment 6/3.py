class converter:
    # conversion of 1 feet to other units
    l= [1,12,0.333,0.0001893,304.8,0.48,0.3048,0.0003048]
    nums=['feet','inches','yards','miles','millimeters','centimeters','meters','kilometers']
    def __init__(self,n,unit):
        self.n=n
        self.unit=unit
        self.index=self.nums.index(self.unit)
    '''
    # convert n*miles ->km
    step 1: by given nums list --> x*miles=y*km --> 1miles=y/x * km
    step 2: n*y/x
    '''
    def feet(self):
        return self.n *( self.l[0]/self.l[self.index])
    def inches(self):
        return self.n *( self.l[1]/self.l[self.index])
    def yards(self):
        return self.n *( self.l[2]/self.l[self.index])
    def miles(self):
        return self.n *( self.l[3]/self.l[self.index])
    def millimeters(self):
        return self.n *( self.l[4]/self.l[self.index])
    def centimeters(self):
        return self.n *( self.l[5]/self.l[self.index])
    def meters(self):
        return self.n *( self.l[6]/self.l[self.index])
    def kilometers(self):
        return self.n *( self.l[7]/self.l[self.index])
n,u=int(input("enter number: ")),input("enter units: ")
c=converter(n,u)
conversn=input("Into which units units u want to convert: ")
print(c.__getattribute__(conversn)())
