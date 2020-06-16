# user defined functions
def square() :
	x= 5**2
	print(x)

square()


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