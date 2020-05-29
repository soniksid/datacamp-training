# making obects iterable using iter() and next()
section = {'roll1': 2, 'roll2': 3}
sec = iter(section)
print(*sec)

# iteration using enumerate():
li = ['a', 'b', 'ab', 'abc']
print(list(enumerate(li)))

# enumerate() with for loop:
class1 = ['zero', 'one', 'two', 'three', 'four']
for index, value in enumerate(class1):
	print(index, value)
