
# Q2. What are list,sets and dictionary how can we create them in python give example and use
# case of each
#  
#Lists are one of 4 built-in data types in Python which is used to store collections of data.
fruits =['apple','banana','mango','berry']
fruits.pop(2)
print(fruits)

# Sets are used to store multiple items in a single variable.
fruits = {'apple','banana','mango','berry','peach','apple','apple'}

fruits.remove('mango')
print(fruits)

# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
my_dict={
    "name":"deepti",
    "age":18,
    "Hobbies":["djsdh","dhjshds"]
}

my_dict["address"]='pokhara'
print(my_dict)

