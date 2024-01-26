#Boolean Logic

#Now it's time to level up our Booleans with some operators,which allow us to combine multiple condition
#let's start with the and operator,it is True,if both condition evaluate to True

print(1==1 and 2==2)

print(1==1 and 1==3)

#Now onto the or operator
#The or operator is True if either (or both) of its condition are True,and False if both condition are False

print(1==1 or 5==7)
print(50*2 >110 or 70//7<5)

#As you can see,besides value,you can also compare variable to form condition:

age=24
limit=18
height=197
if(age > limit and height > 180):
    print("Cool")

#Finally, the not operator works a little differently.not takes just one argument,and inverts it.
#The result of not True is False,and not False goes to True,Like this:
print(not 1==1)
print(not 7<5)

#You can chain multiple comditional statement in an if statement using the Boolean operators.
# For examples
country = "US"
age=50
if (country=="US" or country=="GB") and (age > 0 and age < 100):
    print("Cool")