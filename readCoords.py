# printfile.py
#     Prints a file to the screen.

def main():
    fname = input("Enter filename to get the coordinates of points: ")
    infile = open(fname,"r")
    xList=[]
    yList=[]
    for line in infile:
        x,y=line.split(',')
        xList.append(float(x))
        yList.append(float(y))
    print('The list of x coordinates is', xList)   
    print('The list of y coordinates is', yList)       
main()
