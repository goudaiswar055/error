##dictionaries in python:
##dictionaries are used to store data in key-value pairs.
##they are unordered, changeable and indexed.
###syntax:
##dictionary_name={key1:value1,key2:value2,key3:value3}
# info ={
#     "name": "iswar",
#     "subject":["python","java","c++"],
#     "topics":("data types","operators","loops"),
#     "age": 22,
#     "is_student": True,
#     "marks": 98.99
# }
# print(type(info))
# print(info)


##Nested dictionaries:
# A nested dictionary is a dictionary that contains one or more dictionaries as its values. It is useful for storing structured or hierarchical data.
# student={
#     "name":"iswar gouda",
#     "subject":{
#         "phy":98.99,
#         "chem":99.25,
#         "math":97.55
#     }
# }
# print(student["subject"]["chem"])

##dictionary method:
##myDict.keys()#returns all keys
#myDict.values()#returns all values
##myDict.items()#returns all (key,val)pairs as tuples
##myDict.get("keys"")#returns the key according to value
#myDict.update(newdict)#insert the specified items to the dictionary.


##sets in python:
#set is the collection of the unordered items.
#each element in the set must be unique & immutable.
# nums={1,2,3,4}
# set2={1,2,2,2}
#repeted element stored only once , so it resolved to {1,2}
# null_set=set() #empty set syntax
#set methods:
#add(): adds an element to the set.
#remove(): removes an element from the set.
#discard(): removes an element from the set if it exists.
#pop(): removes and returns an arbitrary element from the set.
#clear(): removes all elements from the set.
#example:add() method:
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(1)
collection.clear()

print(collection.pop(2))


