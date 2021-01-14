# in this new project we will learn about the data structure and algorithm
# there are various built in data structure in python such as list tuple dictionary and array.....
# so lets get started with array

# so the first ques is what is array?
# Answer is the array is a collection of single data items....like this [2,5,4,6] in this array we have a integer
# data type elements... but in a python we can not access array like the other data structures in pytho....we have to
# import a module of array in python....like this:

import array as arr
a = arr.array('i', [2, 3, 4])
b = arr.array('i',[5, 9, 7])
print(a)
# add items in array
# append method for add element
a.append(4)
print(a)
# extend method for add element
a.extend([5,6,7])
print(a)
# concatinate the elements
num = arr.array('b')
num = a + b
print(num)

