#A program to compute the value of investmentcarried 10 years

def main():
    print('This program calculates the future value')
    
    principal = eval(input('Enter the initial principal'))
                     
    apr=eval(input('Enter the annual interest rate:'))
             
    years= eval(input('How many years should we look aheead?'))

    for i in range(years):
        principal = principal * (1+apr)
        print ('The value of your investment in',years,'years is ',principal,'dollars')

main()

            
              
