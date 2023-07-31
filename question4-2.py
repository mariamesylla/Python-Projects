# case where we calculate the slope : ask user for the value of the x and y coordonnate at a
#at different points and return the value of the slope of the line


def main():
    x1,y1= eval(input('Please enter values of the x, y coordinates for the first point separated with comma'))
    x2,y2= eval(input('Please enter values of the x, y coordinates for the second point separated with comma'))
    if x2 != x1:
        m =(y2 - y1) / (x2 - x1)
        print('The slope of the line is ', m)

        b= y1 - m* x1
        print('the equation of the line is ', m, 'x+',b)
    else:
        print('The line is vertical with equation x=',x1)


main()
