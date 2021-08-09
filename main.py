str = 'ashanti is an idiot'
print(str.capitalize())  # capitalise
print(str.count("an", 0, len(str)))  # look for occurence of text in a string

s = str.encode('utf-8', 'strict')
print(s)

##################################################################
print(max(str))
print(min(str))

##################################################################
print(str.replace('ashanti', '---E---', 1))
###################################################################

print(str.upper())

###############################################################

print(str.index('idiot'))

##############################################################

print(str[::-1])  # reverses string
print(str[3:8])  # return
print(str.find('a'))  # returns the index at which the given letter is present in String
print(str + str)  # concatenation of String
print(str * 2)  # also a form of concatenation
str2 = "This is a bullshit story, %s, lets talk about the money %f"
print(str2 % ("Laura", 23.55))
########################################################################################


# Tuple is sequential immutable python objects...just like lists(mutable)
tup1 = ("Hadoop", "Python", "Java")
print(len(tup1))  # gives the total length of the tuple
print(max(tup1))  # returns items with the max value
print(min(tup1))  # returns items from tuple with min value

##tuple - sorting and reversing
tup2 = (1, 3, 4, 5, 2, 78, 3)
print(sorted(tup2))
print(tup2[::-1])

print(len(tup1))  # shows length of tuple
print(tup1 * 2)  # repitition
print("Hadoop" in tup1)  # check if the word is in a text

tup3 = (1, 3, 5, 6, 9)
tup4 = (5, 7, 9, 0, 1)
tup5 = tup3 + tup4  # concatenating tuples - updating tuples
print(tup5)

del tup3  # deleting elements
# print(tup3)

# Difference between Lists and Tuples

list1 = [1, 2, 3, 'John', 'Uber']
print(list1)
list1[2] = 'Rogers'
print(list1)

tup = (1, 2, 3, 'Roger')
print(tup)
# tup[1] = 'Python'  # tuple does not allow this type of change
print(tup)

# A list inside a tuple

tup_list = ([1, 2, 3], [4, 5, 6], [7, 8, 9])  # lists in a tuple
print(tup_list)
print(len(tup_list))  # count of lists in a tuple
print(tup_list[0][0:2])  # slicing return 2 elements from the 1 element
print(tup_list[::-1])  # reversing the ordering of the lists

# Updating tuple
tup_list[0][1] = 90  # you can update a tuple because you are using lists in them
print(tup_list)

# deleting element in tuple
del (tup_list[1][2])
print(tup_list)

# converting tuples into lists
tuple20 = (1, 2, 4, 5, 'Regarere')
lst = list(tuple20)  # converting tuple to list to make changes to the tuple
print(lst)

lst[1] = 'R'
print(lst)

tuple21 = tuple(lst)
print(tuple21)
print(type(tuple21))

# list - indexing and slicing
list1 = ['Hadoop', 'Rust', 'SAS', 'Python']
print(list1[1])  # return index 1
print(list1[0:2])  # return from index 0 and 1 aka the first two indexes
print(list1[-1])  # for an non empty list return the first index from the reverse
print(list1[::-1])  # reverse the list

# list - updating and deleting elements
list3 = ['Python', 'Java', 'Orange']
list3[1] = 'Rose'
print(list3)

del (list3[2])
print(list3)

# remove and pop functions
list4 = [1, 2, 3, 4, 5, 'a', 'b', 'c']
print(list4.pop(3))  # returns the element at a given index

list4.remove('a')
print(list4)

# type()
list5 = [1, 2, 3, 'King', 'Queen']
print(type(list5))

print([x ** 2 for x in [2, 3, 4, 5, 6, 7]])  # loop can be used in print to show
# squares of elements of lists

# lists - built in functions
list6 = [1, 2, 3, "Machine Learning"]
list6.append("Richard")  # add item to the end of the list
print(list6)

list6.extend(['g', 'j'])  # insert many items at the end of list
print(list6)

list6.insert(3, 'Scripting')  # insert an item at a given position
print(list6)

list6.remove(1)  # removes an item from the list
print(list6)

list7 = ['Python', 'Neko', 'Abiola', 'Ola']
print(sorted(list7))  # sorted list
print(list7[::-1])  # reverses the list

# A tuple in a list
list8 = [(1, 2, 3), ("Python", "Mather", "Rage")]  # tuples in a list
print(list8)
print(len(list8))  # count of tuples in a list
print(list8[1][0:1])  # slicing

# list8[0][1] = 50  # using a tuple makes the list immutable TypeError: 'tuple' object does not support item assignment
print(list8)

# Dictionaries - this is an unordered collection of key value pairs. Used when you have
# a huge amount of data

dict1 = {1: 'Heroku', 2: 'Java'}  # creating a dictionary
print(dict1)
print(dict1[1])  # accessing values in dictionaries

# Updating elements

dict1[1] = "Javascript"
print(dict1)

del (dict1[2])  # deleting elements
print(dict1)

# Built in functions of dictionaries
dict2 = {1: 'Python', 2: 'Android'}
print(len(dict2))  # returns the length of the dictionary
# print(str(dict2))  # returns the dictionary as String
print(type(dict2))  # returns type

rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec.get('name'))  # returns the value of the key passed

print(dict2.items())  # returns items in dictionary in the form of tuples
print(dict2.keys())  # returns keys in dictionary
print(dict2.values())  # returns values in dictionary
print(dict2.setdefault(1, 4))

# Methods of dictionaries
dict6 = {1: "Prada", 2: "Gucci"}
print(dict6.copy())  # creates copy of dictionary
dict6.clear()  # deletes all the emelemts in dictionary
print(dict6)

# Sorting Keys for Loops
dic = {3: 'Rosku', 1: 'Python', 2: 'Night'}
ks = list(dic.keys())  # return dictionary keys as a list
print(ks)

sk = sorted(ks)  # sk sorts the keys of the dictionary
print(sk)

for key in sk:
    print(key, '=>', dic[key])  # prints sorted keys with their respective values

# Tuple and List in Dictionary
# tuple in set
dic1 = {1: (1, 2, 3), 2: (3, 4, 5, 6)}  # tuples are given as elements in dictionary
print(dic1)
print(dic1[1][1])  # return index 1 in the dict and the index 1 in the value of key 2

# list in set
dic2 = {1: ('Python', 'Java'), 2: [1, 2, 3, 4]}
print(dic2)
print(dic2[1][0])

# Set is an unordered collection of unique items, Set is defined by values separated by comma
# inside braces()

# Set can also be created by calling the inbuilt in set function:

x = set("Welcome to hell")  # unique values are the rule..duplicates will be removed
print(type(x))
print(x)

# set operation - union
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 9, 10}
print(a | b)  # it will join but remove duplicates

print(a & b)  # intersection: return common elements in the two sets only

print(a - b)  # difference - join and return elements in a but not b

print(b - a)  # difference - join and return elements in b but not a

# more set examples
set1 = {'a', 'b', 'c', 'd'}
set2 = {'a', 'c', 'e', 'd'}

print(set1 | set2)  # union

print(set1 & set2)  # intersection

print(set1 - set2)  # difference

s = {1, 2, 3, 'a', 't'}
set1 = {1, 'a', 'b'}
print(1 in s)  # testing if 1 is in s set

print(set1.issubset(s))  # Returns true if set 1 is a subset of s

print(5 not in s)

print(s.issuperset(set1))  # returns true if s is a super set of set1

print(s.union(set1))

print(s.intersection(set1))

print(s.difference(set1))

print(s.symmetric_difference(set1))

s.add('c')  # add elements to set
print(s)

s.remove(3)  # removes element from set
print(s)

s.discard(9)  # removes element from set if present
print(s)

s.pop()  # removes and returns an arbitrary element from list
print(s)

s.clear()  # removes all element from set
print(s)

# conditional statements
# if

x = 9
y = 23

if (x < y):
    print("X is less than Y")
elif (x > y):
    print("X is greater than Y")
else:
    print("X equals Y")

# While condition will keep running until a condition is met
count = 0
while (count <= 10):
    print(count)
    count = count + 1

print("Testing done")

# for will repeat a group of statements a specified amount of types
for x in (1, 2, 3, 4, 6):
    counter = x * 2
    print(counter)

# we do not know the number of iterations in while loop but in for loop we do.

fruits = ['Banana', 'Rice', 'Apple']
for index in range(len(fruits)):
    print(fruits[index])

# factorial
x = 10
for x in range(10):
    print(x * x)

# Nested Loops
# count=1
# for i in range(10):
#     print(str(i) * i)
#
#     for j in range(10):
#         count=count + 1
#

# Loop Control Statements
# break statement - terminates the loop process and transfers to statement immediately following the loop statement
# continue = causes the loop to skip the remainder of its body and immediately retest
# its condition prior to reiterating
# pass statement - the pass statement in python is used when a statement is required
# syntactically but you do not want any command or code to execute

for i in range(10, 50):
    print(i)
    if(i==30): #return 10 to 50 but break at 30
        break

for j in range(1, 11):
    print(j)
    if(j==5):#return 1 to 11 if j = 5 then retest whether j is between 1 to 11
        continue

k = 4
for k in range(1, 3):
    pass # if k is between 1 to 3 then pass(do not run this loop)
print("Do not run this loop")

#Input - Reading Keyboard Input

inputStr = input("Enter your input")
print("Your input is "+ inputStr)

#Opening and Closing Files

#Opening a file
#To manipulate a file in python you need top open it

spec_char = []
for i in range(35, 65):
    spec_char.append(chr(i))
print(spec_char)



