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

