# Determine adults and writing to a file

def main():
    print("This program creates a file of adult customers from a")
    print("file of customers.")
    print("The format of the file is assumed to be: name lastname age gender")
    print("Adults are takeng to be when age >= 18")
    print()

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the adult customers go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        L = line.split()
        
        # create the username
        if int(L[2]) >= 18:
            print(' '.join(L), file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Adult customers have been written to", outfileName)

main()
