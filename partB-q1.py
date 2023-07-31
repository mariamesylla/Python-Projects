import random
class Card: 
    def __init__(self, rank, suit):
        self._suit = suit
        self._rank = rank
        
  
    def getSuit(self):
        return self._suit
    
    def printCard(self): 
        print(self._rank,"of",self._suit)

    def getRank(self):
        return self._rank
    
    def shuffle(self): 
         ranks = ["Ace","King","Queen","Jack","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
         suits = ["Diamond","Club","Spade","Heart"]
         self._rank = ranks[random.randint(0,12)]
         self._suit = suits[random.randint(0,3)]
         
    def cheat(self,rank, suit):
        self._rank = rank
        self_suit = suit
        
c = Card("Ace","Spade") 
print(c.getRank())
print(c.getSuit()) 
c.printCard() 
c.shuffle() 
c.printCard() 
c.cheat("King", "Heart") 
c.printCard() 
 
