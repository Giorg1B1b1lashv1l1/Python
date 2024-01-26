#Loops  

#Loops allow you to repeat a block of code multiple times.

#While Loops

#Here's while loop containing a variable that counts up from 1 to 5,at which point the loop terminates.
i=1
while i < 5:
    print(i)
    i=i+1
print("Finished!")

#The code in the body of a while loop is executed repeatedly while the condition is True
#This is called iteration
sum = 0 
x = 10 
while x > 0:
    sum+=x
    x-=1
print(sum)

#You can also use other statement , such as if statement in loops,this is especially useful in things like games,where you might need to loop through a number of players action and add or remove points to the players's score.
#Check out this code,which uses an if/else statement inside a while loop to separate the even and odd numbers in the range of 1 to 10:

x = 1 
while x < 10:
    if x%2 == 0 :
        print(str(x) +" is even")
    else:
        print(str(x) + " is odd")
    x+=1