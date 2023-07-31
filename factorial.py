
# Here is the introduction
# factorial.py

def main():
    print("Incorrect Factorial")
    print ()
    n = int(input("Enter a whole number: "))
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print ()
    print("The factorial of ", n, " is ", fact)


main()

