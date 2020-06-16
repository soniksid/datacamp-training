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


# function for understanding basic concept of nonlocal
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


# to get list of builtin errors, use:
print(dir(locals()['__builtins__']))