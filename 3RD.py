##list in python:
# a built in data type that stores set of values.
## it can store elements of different data types(integers,flots,strings,boolean values)
# marks1= 94.5
# marks2= 90.5
# marks3= 88.5

# marks=[marks1,marks2,marks3]
# print(marks)
# print(type(marks))
# print(len(marks))



##strings are immutable in python: we can't change the value of a string after it has been created.
## list is mutable in python: we can change the value of a list after it has been created.

# student=["iswar",96.99,"odisha"]
# print(student[0])
# student[0]="ganga"
# print(student[0])


##similar to string slicing we can slice a list to access a range of elements from a list using their index values.
##list_name[starting_idx:ending_idx:step]##endind index is not included in the output.
# marks=[98,89,90,95,88]
# print(marks[1:4])                ##output: [89, 90, 95]
# print(marks[0:len (marks):2])    ##output: [98, 90, 88]
# print(marks[-3:-1])              ##output: [90, 95]


##list methods: list methods are built in functions that can be used to perform various operations on a list.

# append(): adds an element to the end of the list.
# sort(): sorts the elements of the list in ascending order.
# reverse(): reverses the order of the elements in the list.
# insert(): adds an element at a specific index in the list.
# remove(): removes the first occurrence of an element from the list.
# pop(): removes and returns the element at a specific index from the list.

##append() example:
# list=[1,2,3,4,5]
# list.append(8)
# print(list)

##sort() example:
# list=[5,2,8,1,4]
# list.sort()
# print(list)
# print(list.sort())##output: None

##reverse() example:
# list=[1,2,3,4,5]
# list.reverse()
# print(list)
# print(list.reverse())##output: None

##insert() example:
# list=[1,2,3,4,5]
# list.insert(2,8)
# print(list)
# print(list.insert(2,8))##output: None

##remove() example:
# list=[1,2,3,4,5]
# list.remove(3)
# print(list)

##pop() example:
# list=[1,2,3,4,5]
# list.pop(2)
# print(list)


##tuple in python:

# a built in data type that stores set of values.
# a tuple is similar to a list but it is immutable.
# tuples are immutable in python: we can't change the value of a tuple after it has been created.
# tuple_name=(element1, element2, element3, ...)
# tuple_name=(element1,)  ##single element tuple

# tup=(1,2,3,4,5)
# print(tup)
# print(type(tup))
# print(len(tup))
# print(tup[0])
# print(tup[1])
# tup[0]=10 ##output: TypeError: 'tuple' object does not support item assignment

# tup=("1")
# print(tup)
# print(type(tup)

##slicing in tuple:
# similar to string slicing we can slice a tuple to access a range of elements from a tuple.
# tuple_name[starting_idx:ending_idx:step]

# example:
# tup=(1,2,3,4,5)
# print(tup[1:4])  ##output: (2, 3, 4)

##tuple methods:
 #  tuple methods are built in functions that can be used to perform various operations on a tuple.

# count(): returns the number of occurrences of an element in the tuple.
# index(): returns the index of the first occurrence of an element in the tuple.

# tup=(1,2,3,4,5,1,2,3,4,5)
# print(tup.index(5))
# print(tup.count(1))



##wap to ask the user t enter names of their 3 favorite movies & store them in list & print the list.

# movies=[]
# movie1=input("enter 1st favorite movie: ")
# movie2=input("enter 2nd favorite movie: ")
# movie3=input("enter 3rd favorite movie: ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

##or
# movies=[]
# movies.append(input("enter 1st favorite movie"))
# movies.append(input("enter 2nd favorite movie"))
# movies.append(input("enter 3rd favorite movie"))
# print(movies)

## wap to check if a list contains a palindrome of elemenrts.
# list=[1,2,3,2,1]
# list2=list.copy()
# list2.reverse()
# if(list==list2):
#     print("palindrome")
# else:
#     print("not palindrome")

##or

# list1=[1,2,3,2,1]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")

