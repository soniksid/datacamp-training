# making obects iterable using iter() and next()
section = {'roll1': 2, 'roll2': 3}
sec = iter(section)
print(*sec ,"\n")


# iteration using enumerate():
li = ['a', 'b', 'ab', 'abc']
print(list(enumerate(li)), "\n")


# enumerate() with for loop:
class1 = ['zero', 'one', 'two', 'three', 'four']
for index, value in enumerate(class1):
	print(index, value)


# iteration using zip():
class2 = ['zero', 'one', 'two', 'three', 'four']
li1 = ['a', 'b', 'ab', 'abc']
result = zip(class2, li1)
result_list = list(result)
print(result_list)


# zip() using for loop:
class2 = ['zero', 'one', 'two', 'three', 'four']
li1 = ['a', 'b', 'ab', 'abc']
for num1, num2 in zip(class2, li1):
	print(num1, num2)


#  printing even numbers using list comprehensions
list1 = [22, 23, 24, 25, 26, 28, 30]
new_list = [num for num in list1 if num % 2 == 0]
print(new_list, "\n")


#  printing even square numbers using dictionary comprehensions
list1 = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14]
new_list = {num:num**2 for num in list1 if num % 2 == 0}
print(new_list, "\n")


#  printing even numbers using generator comprehensions
list1 = [22, 23, 24, 25, 26, 28, 30]
new_list = (num for num in list1 if num % 2 == 0)
for num in new_list:
	print(num, end=" ")


