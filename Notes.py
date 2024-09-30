
'''
    Lesson: String Manipulation
    Author: Mr. Kalisz
    Date Created: Sept 30, 2024
    Date Last Modified: Sept 30, 2024

'''

#Methods vs Functions

#Functions - A procedure that returns one thing
#Methods - A procedure associated with an object that returns one thing

#upper - Method
#creates a copy of the String with all uppercase characterds

word = "Hello World"

print(word.upper())
print(word)

#If you want to change the original variable, you need to assign to it

word = word.upper()
print(word)

#lower
#creates a copy of the String with all lowercase characters

word = "Hello World"

print(word.lower())
print(word)

#If you want to change the original variable, you need to assign to it

word = word.lower()
print(word)

#len - Length of the string in characters
# Function - It is not associated with an object 

print(len(word))


#INDEXES
#Location of a data in programming
#For a string - this is the location of a character inside of a string

#These locations start at 0
#H E L L O   W O R L D
#0 1 2 3 4 5 6 7 8 9 10

# index - Returns the index of the provided string
# Method - is associated with a string

print(word.index("h"))
print(word.index("world")) #Gives the index of the FIRST letter of the string
print(word.index("l")) #Return the first occurance of the letter
print(word.index("W")) #Runtime error when the string can't be found

# splicing - Gets a copy of a substring (part of a string), based on index values
# Starting Index - Inclusive - includes the value at the index
# Ending Index - Exclusive - excludes the value at the index


print(word[0:5])
# EndingIndex - StartingIndex = Length of our substring

print(word[6:]) #not specifying an ending index goes to the end of the string
print(word[:5]) #Not specifying a starting index starts from the beginning of the string

print(word[5:5]) #Anytime the starting index and ending index cross over there is an empty string result
print(word[4]) #Without a colon it gives just a single character
# print(word[15]) #An index that doesn't exist causes a runtime error
print(word[0:15]) #In the context of a splice it will still work

#ONLY IN PYTHON

print(word[3:-1]) #Negative numbers count backwards from the end of the string
print(word[-3:])

