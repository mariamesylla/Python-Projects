# Program: Fraction.py
# 
#
from gcd import gcd

class Fraction:

  def __init__(self, numerator=0, denominator=1):#default is 0/1
    if denominator == 0:                   # fraction is undefined
      self._numer = 0
      self._denom = 0
    else:
      factor = gcd( abs(numerator), abs(denominator) )
      if denominator < 0:                  # want to divide through by negated factor
        factor = -factor
      self._numer = numerator // factor #two protected attributes
      self._denom = denominator // factor

  ########  Arithmetic Methods  ########
  def __add__(self, other):#__add__ it overwrites the usual + in numbers
    return Fraction(self._numer * other._denom + other._numer * self._denom, self._denom * other._denom)

  def __sub__(self, other): #work when you put the -
    return Fraction(self._numer * other._denom - other._numer * self._denom, self._denom * other._denom)
   

  def __mul__(self, other): 
    return Fraction(self._numer * other._numer, self._denom * other._denom)

  def __truediv__(self, other): # multiplication by reciprocal
    return Fraction(self._numer*other._denom, self._denom*other._numer)

  ########  Comparison Methods  ########
  def __lt__(self, other):
    return self._numer* other._denom < self._denom * other._numer
  

  def __eq__(self, other): #overwrites  ==
    if self._numer == other._numer and self._denom == other._denom:
      return True
    else:
      return False

  ########  Type Conversion Methods  ########
  def __float__(self):
    return float(self._numer) / self._denom

  def __int__(self):
    return int(float(self))                # convert to float, then truncate
  
  def __str__(self):
    if self._denom == 0:
      return 'Undefined'
    elif self._denom == 1:
      return str(self._numer)
    else:
      return str(self._numer) + '/' + str(self._denom)



if __name__ == '__main__':
  F1 = Fraction(-3,4)
  F2 = Fraction(1,-5)
  print('The first fraction:', F1)
  print('The second fraction:', F2)
  print('The sum:', F1+F2)
  print('The difference:', F1-F2)
  print('The multiplilcation:', F1*F2)
  print('The division:', F1/F2)
  print('Are they equal?',F1 == F2)
