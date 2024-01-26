#If Statement

#One thing you can do with booleans is use if statment to run code based on a certain condition,say,if the boolean evalutes to True

#An if statment looks like this:
#if condition:
    #statment

#Python uses indentation(that empty space at the beginning of a line) to delimit blocks of code.depending on the program's logic,indentation can be mandatory

#The statement in the if should be indented

#If statement example:
x=50
if x>20:
    print("x is greater then 20")


#The colon at the end of the expression in the if statement is important,don't leave it out

age = 20
if age > 18:
    print("cool")


#Sometimes we'll have to perform more complex checks.but that's no problem,becouse if statement can be nested,one inside the other.
#For Example:
num=8
if num > 5 :
    print("Bigger than 5")
    if num <=50:
        print("Beetwen 5 and 50")    \
        
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num ==7:
            print("7")