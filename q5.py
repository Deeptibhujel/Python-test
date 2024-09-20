
name= input("Enter your name:")
age = input("Enter your age:")
    

with open("my file.txt","w") as file:
    file.write(name)
    file.write(str(age))
print("Writing success!!")

with open ("my file.txt","r")as file:
    name = file.read()
    age = file.read()

print(name)
print(age)