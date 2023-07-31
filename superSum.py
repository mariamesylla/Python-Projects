# question 5

def superSum(aList):
    s = 0
    for i in range(len(aList)):
        s += aList[i]*(len(aList)-i)
    return s

if __name__ == '__main__':
    print(superSum([1,2,3,4,5]))
        
