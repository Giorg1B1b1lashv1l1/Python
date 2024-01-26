#In-place Operators

#In-place operators let you write code like "x=x+3" more concisely,as "x+=3"

#1
x=2
print(x)
x+=3
print(x)

#2
x=8
print(x)
x*=4
print(x)

#3
x=7
print(x)
x-=5
print(x)

#4
x=18
print(x)
x/=6
print(x)

#5
x=10
print(x)
x**=2
print(x)

#You can also use in-place operators for string concatenation
x="hello "
print(x)
x+="world"
print(x)

#We have covered a number of important topics, such as variables,input and operators.
#these can be used together to make a more complex program.

#For example,let's make a program that takes miles as input and output the corresponding km value

miles=int(input())
km=miles * 1.60934

print(km)