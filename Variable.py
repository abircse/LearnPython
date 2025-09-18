
# === Assign Multiple Values to Variable === #
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# === Mutable Variable === #
x = 4
x = "Nayeem"
print(x)

# === Output Variable (Using Comma) === #
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# === Output Variable (Using + Sign) === #
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# === Output Variable (With Arithmatic Operation)
x = 5
y = 10
print(x + y)

# === Variable Casting === #
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# === Global Variable in outside of function === #
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# === Global Scope Variable === #
def myfunc():
  global x
  x = "Josh"

myfunc()
print("Python is " + x)