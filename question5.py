#eligibility 

age = int(input("Enter the age :"))
citizen = int(input("Enter years of citizenship :"))

if age>=30 and citizen>=9:
    print("The person is eligible to be US Senator and US representative")
elif age>=25 and citizen>=7:
    print("The person is eligible to be US representative")
else:
    print("The person is not eligible to be US Senator and US representative")
