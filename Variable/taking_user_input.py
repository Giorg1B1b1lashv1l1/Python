#Input
#Some programs need to take input from the user for example, a game can ask for the user's name and age as input and then use them in the game.
#The input() function prompts the user for input,and return what they enter as a string.
#Like this:
x=input()
print(x)

#Even if the user enters a number as input,it's processed as a string
x=input()
print("You entered: "+x)

#You can provide a string to input() between the parenthese,producing a prompt message
#For example:
name=input("enter your name: ")
print("my name is " + name)



#Working with input

# So we know that the input() function returns a string.But what if we need it to be something else,like a number? no problem, we can totally do that

#Let's assume we've taken the age of the user as an input.

#So convert it to a number,we can use the int() function

age=int(input())
print(age)

#Similar to the int() function, the float() function converts a string to a float

height=float(input())
print(height)

#Sometimes there is a need to use a number in a string concatenation.

#This can be done useing str() function, which converts a number to a string

age=20
print("I'm " + str(age) + "years old")

#The last thing to mention is that you can use input() multiple times to take multiple user inputs.
#For examples:

name=input()
age=input()
print(name + "is " + age)