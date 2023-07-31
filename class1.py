#This a our first time doing scripts

#our first function

def goodday():
    print('Good Day')
    print('How are you?')



#our second function


def goodevening(name):
    print('Good evening',name)
    print ('Hey '+ name+' How about coffee!!!')


#our third function
'''
def main():
    print("This program illustrates a chaotic function")
    x=eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x+ 3.9 * x * (1-x)
        print (x)

main()
'''
#our fourth function


def main():
    print("This program illustrates a chaotic function")
    x=eval(input("Enter a number between 0 and 1: "))
    if x>0 and x<1:
        for i in range(10):
            x= 3.9*x*(x-1)
            print(x)
    else:
        print("your number x is out of range")
        

main()

