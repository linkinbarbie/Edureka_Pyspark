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

list8[0][1] = 50  # using a tuple makes the list immutable
print(list8)

# Dictionaries - this is an unordered collection of key value pairs. Used when you have
# a huge amount of data

dict1 = {1: 'Heroku', 2: 'Java'}
print(dict1)
print(dict1[1])
