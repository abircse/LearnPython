# DATA TYPE
# Name: Text || Type: str
# Name: Numeric || Types:	int, float, complex
# Name: Sequence || Types:	list, tuple, range
# Name: Mapping || Type:	dict
# Name: Set ||  Types:	set, frozenset
# Name: Boolean ||  Type:	bool
# Name: Binary || Types:	bytes, bytearray, memoryview
# Name: None || Type: NoneType


# Method to find which variable belogs in which data type
x = ["apple", "banana", "cherry"]
print(type(x)) # You can pass any type of data type in type function

# == Example of Different Data Type == #
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

# == Example of Specify Data Type == #
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview


# ==== 
# 
# SOME EXAMPLE : DATA TYPE
# 
# ===== #

# == Array to store any type of data type in same array == #
x = ['Apple', 'Banana', 0.6]
print(x)

# == DICTIONARY FOR KEEP KEY PAIR VALUE  == #
x = dict(name="John", age=36)
print(x.get('name'))

# == SET TO STORE ANY TYPE OF DATA (Mutable) == #
x = set(("apple", 1, "cherry"))
print(x)

# == SET TO STORE ANY TYPE OF DATA (Imutable) == #
x = frozenset(("apple", "banana", "cherry"))
print(x)

# Bolean Value
x = bool(1)
print(x)
y = bool(0)
print(y)

# Type Conversion / Type Casting

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
# print result
print(a)
print(b)
print(c)


# 
# Generate Random number
# NOTE: Here generating a number from rang 1 to 10
#  
import random
print(random.randrange(1, 10)) 

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multi Line / Single qoutes  (comma will be used for separate string as line)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Get String Char position like array
a = "Hello, World!"
print(a[1])

# Check String available in text  
txt = "The best things in life are free!"
print("free" in txt)

# Check String Not in text
txt = "The best things in life are free!"
print("expensive" not in txt)

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

# Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])

# Modify String
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())

# Removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String (Seprate string before comma & after comma as separate string)
a = "Hello,World!"
print(a.split(","))

# String Concatanation
a = "Hello"
b = "World"
c = a + b
print(c)

# String Concatanation with a space between word
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Formated String
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Boolen will return false in this scope
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# === String Methods
# best for use in programming/api/other purpose
# 
#  === ##
capitalize()	#Converts the first character to upper case
casefold()	#Converts string into lower case
center()	#Returns a centered string
count()	#Returns the number of times a specified value occurs in a string
encode()	#Returns an encoded version of the string
endswith()	#Returns true if the string ends with the specified value
expandtabs()	#Sets the tab size of the string
find()	#Searches the string for a specified value and returns the position of where it was found
format()	#Formats specified values in a string
format_map()	#Formats specified values in a string
index()	#Searches the string for a specified value and returns the position of where it was found
isalnum()	#Returns True if all characters in the string are alphanumeric
isalpha()	#Returns True if all characters in the string are in the alphabet
isascii()	#Returns True if all characters in the string are ascii characters
isdecimal()	#Returns True if all characters in the string are decimals
isdigit()	#Returns True if all characters in the string are digits
isidentifier()	#Returns True if the string is an identifier
islower()	#Returns True if all characters in the string are lower case
isnumeric()	#Returns True if all characters in the string are numeric
isprintable()	#Returns True if all characters in the string are printable
isspace()	#Returns True if all characters in the string are whitespaces
istitle()	#Returns True if the string follows the rules of a title
isupper()	#Returns True if all characters in the string are upper case
join()	#Joins the elements of an iterable to the end of the string
ljust()	#Returns a left justified version of the string
lower()	#Converts a string into lower case
lstrip()	#Returns a left trim version of the string
maketrans()	#Returns a translation table to be used in translations
partition()	#Returns a tuple where the string is parted into three parts
replace()	#Returns a string where a specified value is replaced with a specified value
rfind()	#Searches the string for a specified value and returns the last position of where it was found
rindex()	#Searches the string for a specified value and returns the last position of where it was found
rjust()	#Returns a right justified version of the string
rpartition()	#Returns a tuple where the string is parted into three parts
rsplit()	#Splits the string at the specified separator, and returns a list
rstrip()	#Returns a right trim version of the string
split()	#Splits the string at the specified separator, and returns a list
splitlines()	#Splits the string at line breaks and returns a list
startswith()	#Returns true if the string starts with the specified value
strip()	#Returns a trimmed version of the string
swapcase()	#Swaps cases, lower case becomes upper case and vice versa
title()	#Converts the first character of each word to upper case
translate()	#Returns a translated string
upper()	#Converts a string into upper case
zfill()	#Fills the string with a specified number of 0 values at the beginning

