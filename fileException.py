#open file secure

fileName = input('Enter file name')

try:
    infile=open(fileName,'r')
    print('Get it')
except FileNotFoundError:
    print('Not such file!')
