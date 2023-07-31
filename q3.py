def SumNSquares(n):
    S = 0
    for i in range(1,n+1):
        S += (i*i)
    return S

def main():
    n = int(input('Enter a positive integer: '))
    print('The sum of the squares of the natural numbers up to',n,'is',SumNSquares(n))


main()
