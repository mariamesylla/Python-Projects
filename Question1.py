#sequence

def seq(n):

    if(n == 1):
        return 2
    
    if(n == 2):
        return 3
    
    result = 2 * seq(n-1) + seq(n-2)
    
    
    return result


num = int(input("Please enter a natural number: "))

print("The" ,num,"-th number of the sequence is: " ,seq(num))
