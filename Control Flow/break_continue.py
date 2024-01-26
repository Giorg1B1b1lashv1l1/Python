#Break

#To end a while loop prematurely,we can use a break statement.
#For examples we can break an infinite loop if some condition is met

i=0
while True:
    print(i)
    i=i+1
    if i>5:
        print("Breaking")
        break
print("finished")

#Continue

#Another statement that can be used within loops is continue.
#Unlike break,continue jumps back to the top of the loop,rather than stopping it.Basically,the continue statement stops the current iteration and continue with the next one.

i = 0
while i<5:
    i +=1
    if i ==3:
        print("Skipping 3")
        continue
    print(i)