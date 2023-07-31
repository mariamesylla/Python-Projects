# A program that computes the real roots of a quadratic equation.

#Illustrates use of math library

#NOTE: The program crashes if there is no real root for the equation

import math #It makes the math library available

def main():
    print('This program finds real roots to a quadratic equation')
    print()#to create empty line

# float allows the use of decimal

    a=float(input('Enter coefficient a: '))
    b=float(input('Enter coefficient b: '))
    c=float(input('Enter coefficient c: '))

   
    discroot = math.sqrt(b*b - 4*a*c)
    root1=(-b+discroot)/(2*a)
    root2=(-b-discroot)/(2*a)
    print()
    print('The roots are ' ,root1,root2)

main()

