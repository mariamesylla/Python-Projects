


infile = open('numbers.txt', 'r')
outfile = open('positive.txt', 'w')
line = infile.readline( )

while line != '':
    x = int(line)
    if (x > 0):
        outfile.write(line)

    line = infile.readline( )
infile.close( )
outfile.close( )

    
        
