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