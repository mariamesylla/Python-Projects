fil = open("numbers.txt", "w")

sum = 0

while True:
    num = input("Pleasw enter number and hit enter after the last): ")

    if num == "":
        break

    sum += float(num)

    fil.write(num + "\n")

fil.write("The sum of your numbers is " + str(sum))
fil.close()

print("The sum of your numbers is ", sum)
