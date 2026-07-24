print("my name is iswar")



##variable
##variable is a name given to a memory location in a program
name="iswar"
age=23
price =25.99
age2= age
print(age2)

##data type

print(type(name))
print(type(age))
print(type(price))

##int
##str
##float
##bollean
##none


##keyword:keyword are reserved words in python.


##print sum of two number.
a=2
b=5
sum=a+b
print(sum)

## type of operators
## an operators is a symbol that performs a certain operation between operands.
## 1. arithmetic operator
## 2. relational operator
## 3. assignment operator
## 4. logical operator(not,or,and)

# arithmetic operator
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

##relational operator
a=40
b=10
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)


##assignment operator
num=10
num=num+10 ##10+10=>20(num+=10)
print("num:",num)

##logical operator
a=50
b=30
print(not False)
print(not(a>b))

val1=False
val2=False
print("AND operator:",val1 and val2)
print("OR operator :", (a==b)or(a>b))

##type conversion
a=2
b=4.35
sum=a+b
print(sum)

#type casting
a=float("2")
b=4.25
print(type(a))
print(a+b)


##input in python

##input()statement is used to accept values from user
#input() result for input ()is always a str
#int (input())#int 
#float(input())float

name=input("enter name :")
age=int(input("enter age :"))
mark=float(input("enter mark:"))

print("wewlcome ",name)
print("age:",age)
print("mark=",mark)
