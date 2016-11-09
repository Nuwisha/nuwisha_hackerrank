link = "https://www.hackerrank.com/challenges/string-validators"

# ---=== SOLUTION ===---
data = input()
print(any([c.isalnum() for c in data]))
print(any([c.isalpha() for c in data]))
print(any([c.isdigit() for c in data]))
print(any([c.islower() for c in data]))
print(any([c.isupper() for c in data]))

# ---=== ONELINER ===---
# by Nissen96

# uses all five string methods on each character in input string
# prints True if at least one character made the method return True
print "\n".join([str(any(i)) for i in (list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in raw_input()])))])
or a little less cluttered (perhaps):
# user input
s = raw_input()

# uses all 5 methods on each character and creates a list for each,
# containing the results of each method used on the character.
newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]

# rotates lists clockwise to get lists of each method instead
rotated = list(zip(*newList))

# prints whether or not a True is present for each List
print "\n".join([str(any(i)) for i in rotated])
Example to clarify:
stdin: P12A
s = P12A

# each method is used on each character
newList = [[True, True, False, False, True ] # methods used on P
           [True, False, True, False, False] # methods used on 1
           [True, False, True, False, False] # methods used on 2
           [True, True, False, False, True]] # methods used on A

# rotates clockwise to get lists of methods' returned values
rotated = [[True,  True,  True,  True ] # results for .isalnum()
           [True,  False, False, True ] # results for .isalpha()
           [False, True,  True,  False] # results for .isdigit()
           [False, False, False, False] # results for .islower()
           [True,  False, False, True]] # results for .isupper()

# prints whether or not a True is present for each list
stdout:
True
True
True
False
True

# ---=== TASK ===---
task = """
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum() 
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha() 
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit() 
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower() 
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper() 
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""
