#Booleans

#Booleans can have two value:True and False

#We can create booleans by comparing values,by using the equal operator ==.
#Like this:
my_boolean= True
print(my_boolean)

print(2==3)

print("hello" == "hello")

#The boolean data type has one of only two possible value: True and False.
#Note,that the value must start with a capital letter.
open=True
closed=False


#Comparison
#booleans are created when comparing values,Python has a number of comparison operators:
#equal to- == , not equal to- != , greater than- > , smaller than- < , greater or equal to- >= , smaller or equal to- <=.

#Let's look at some examples

x=8

print(x!=9)
print(x>5)
print(x<2)
print(x>=8)
print(x<=8)


#Greater than and smaller than operators can also be used to compare string lexicographically(the alphabetical order of words is based on the alphabetical order of their component letters)
print("a" < "b")
print("Bob" < "Dave")

#The True and False boolean values can be represented as integers 1 and 0, respestively

x=(10>4)
print(int(x))

y=(25>50)
print(int(y))