# adding the sum to a file
from superSum import superSum

def addingToFile():
    myFile = input('Enter the name of the file where you have the numbers; ')
    source = open(myFile, 'r+')
    aList = []
    for line in source:
        print(line[:-1])
        aList.append(float(line[:-1])) #eliminates the \n at the end of each line
    print(aList)
    source.write(str(superSum(aList)))
    source.close()


if __name__ == '__main__':
    addingToFile()
