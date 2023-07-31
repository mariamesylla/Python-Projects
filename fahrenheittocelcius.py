#A program to convert fahrenheit temperature to celcius


def main():
    fahrenheit= eval(input('What is your Fahrenheit temperature?'))
    celcius = 5*(fahrenheit-32)/9

    print('The temperature is ', celcius , 'degrees celcius.')

main()

