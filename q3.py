# Q3. Write a program that perform Division operation between 2 numbers , use Exception
# handling to handel runtime errors (5)
# E.g user can enter 2 numbers in a,b variables and the program will perform division ans=a/b handel division by 0
# exception

a= int( input("Enter a number"))
b= int(input("Enter a second number"))

try:
    ans= a/b
    print(ans)
except Exception as e:
    print(e)

finally:
    print("Hello world")