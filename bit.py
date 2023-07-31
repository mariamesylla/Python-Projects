# bit Class
class Bit:

    def __init__(self,v=0):
        self.v = v

    def flip(self):
        self.v = (self.v + 1) % 2

    def __str__(self):
        return str(self.v)

def flipBits(aListOfBits):
    for i in aListOfBits:
        i = i.flip()

def printBitList(aListOfBits):
    for i in aListOfBits:
        print(i)

            
