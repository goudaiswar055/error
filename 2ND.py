##string and conditional statements:

##string: string is data type that stores a sequence of charaters.

# str1="this is a string"
# len1=len(str1)
# print(len1)

# str2="iswar is a string"
# len2=len(str2)
# print(len2)

# str3="my name is iswar"
# len3=len(str3)
# print(len3)
# print(str1+str2+str3)## concatenation of string


#str4="GANGA"
# str5="GOUDA"
# final_string=str4+" "+str5
# print(final_string)
# print(len(final_string))


# : indexing is a process of accessing individual characters of a string using their index values.
# str="iswar gouda"
# print(str[0])
# print(str[6])

#slicing is a process of accessing a range of characters from a string using their index values.
# str[starting_idx:ending_idx:step]

# positive indexing: 0,1,2,3,4,5,6,7,8,9,10


# str="iswar gouda"
# print(str[3:len(str)])
# print(str[0:len(str):2])

# negative indexing: -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11
# str="apple is a food"
# print(str[-5:-1])
# print(str[-8:-2:2])


#wap  to input ussers first name &print its length.

# first_name=input("rahul")
# print(len(first_name))

# name=input("enter your name:")
# print("length of your name is:",len(name))

##conditional statements: conditional statements are used to perform different actions based on different conditions.
##syntax:
##if condition:
# statement1
# elif condition:
# statement2
# else:
# statementN

# light="yellow"
# if light=="red":
#     print("stop")
# elif light=="yellow":
#     print("get ready") ##indentation is important in python
# elif light=="green":
#     print("go")
# else:
#     print("invalid light color")


##nesting of if statements: nesting of if statements means placing one if statement inside another if statement.
# age=int(input("enter your age:"))
# if(age>=18):
#     print("you are eligible to vote")
#     if(age>=18 and age<=25):
#         print("you are young voter")
#     elif(age>25 and age<=60):
#         print("you are adult voter")
#     else:
#         print("you are senior citizen voter")

##wap to check if a number entered by The user is odd or even.
# num=int(input("enter a number"))
# if(num%2==0):
#     print("even number")
# else:
#     print("odd number")

##wap to find the greatest of three numbers entered by the user.

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# if(a>=b and a>=c):
#     print("first number is greatest")
# elif("b>=c "):
#     print("second number is greatest")
# else:
#     print("third number is greatest")
      
    ##wap to check if a number is a  multiple of 8 or not.

# x=int(input("enter a number:"))
# if(x%8==0):
#     print("multiple of 8")
# else:
#     print("not a multiple of 8")
    