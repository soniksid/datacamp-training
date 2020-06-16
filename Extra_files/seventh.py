# user defined functions

def sid() :
	x= 5**2
	print(x)

sid()

# function for squaring any no. 
def square(value) :
	x= value ** 2
	return x
y = square(12)
print(y * 2)

# function for raise to pwer (with two parameters for)
def raise_to(value1, value2):
	x= value1 ** value2
	return x
y= raise_to(5, 3)
print(y)

# fuction for returning multiple values using tuples
def raise_both(num1, num2):
	x1= num1 ** 2
	x2= num2 ** 3
	y= (x1, x2)
	return y
z=raise_both(5, 3)
print(z)

# functions using global scope
value=20
def square(num):
	global value
	value= value**2
	return value
print(square(3))

# Nested functions to print any value to its square or cube
def raise_value(n):
	def inner(x):
		y= x ** n
		return y
	return inner
square = raise_value(2)
cube = raise_value(3)

print(square(5))
print(cube(4))




def calc(x, y=5):
	z = x + y
	return z

print(calc(6, 10))



def multiply(value):
	x = 10 * value
	return x

print(multiply(2))


def func():
	a = 1
	b = 2
	def nested_func():
		# a = 5 : This assignment of 5 into 'a' is read only. It is not overwriting the value of 'a'. To overwrite it, we must follow this step:
		nonlocal a
		a = 5
		print(a + b)
	nested_func()
	print(a)

func()
print(5)

# Lambda functions
c = lambda a, b : a*4/b
print(c(5, 4))


# to get the builtin errors, use:
print(dir(locals()['__builtins__']))