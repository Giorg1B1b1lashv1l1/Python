#Else Statement

#The else statement can be used to run some statement when the condition of the if statement is False

x=4
if x == 5:
    print("Yes")
else:
    print("No")

#As with if statement,the code inside the block need to be indented.
#The colon at the end else keyword is important,don't leave it out
    
#Evry if condition block can have only one else statement.
#so for us to make multiple checks,we need to chain if and else statement.
#for example,the following program checks and output num variable's value as text
    
num=3
if num==1:
    print("one")
else:
    if num ==2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("something else")

#Too many if/else statement make your code long and hard to read,
#The best way to solve this is the elif(short for else if)statement,it's a shortcut to use when chaining togehter if and else statement, makeing the code shorter and easier to read.
#The same examples from the previous part can be rewritten using elif statement:
num=8
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("something else")


#And as you see in the previous lesson examples, a series of if elif statement can have a final else block,which is called if none of the if or elif expression is true
 