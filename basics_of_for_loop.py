x = ("a","b","c")

print(type(x))

for x in x:
    print(x)

y = [1,2,43,5]

print(type(y),"type of y")


z = {1,2,3,4567,78}

print(type(z),"the type of z")



a = {1:"2",2:"4"}

print(type(a))



a = [1,2,3,4,5,6]
for x in a:
    print(x,"the value of x")

a = ["bharathithasan","parimelalagar","jothivarman","luso"]

for x in a :
    print("the value of second x",x)


word = "bharathithasan"

for letter in word:
    print("the value of letter",letter)


# using for loop the range:
    
for number in range(5):
    print(number)


iterating over a dictonary

age = {"john":30,"alice":25,"bob":35}

for name, age  in age.items():
    print(name,"this is my friends name")
    print(age,"this is my friends age")



enumerate

fruites = ["apple","banana","cherry"]

for index,fruites in enumerate(fruites):
    print(f"index{index}:{fruites}")

    by using enumerate we can find the index



# using zip()

#using zip we can join the two tupples


name = ["bharathi","kalai","mosas",1]

ages = [30,25,10]

for name,age in zip(name,ages):

    print(f"{name},{ages}")


# let try in list
    
name = {"jolo","heli"}

age = {1,2,4}


for name,age in zip(name,age):

    print(f"{name},{age}")