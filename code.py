import os

def hello(a_name):
	print("Hello, " + a_name)


def hello2(name_a, name_b):
	print("Hello, " + name_a + " and " + name_b)


my_name = "Jan-Erik!"
hello(my_name)
print("Beneath this message you shall see if your code has worked! :)") 
print("")


def sum_two(x,y):
	z = x + y
	return z

def my_sum(a_list):
	total = 0
	for n in a_list:
		total = total + n
	return total


def my_prod(a_list):
    total = 1
    for n in a_list:
        total = total * n
    return total


def length(a_list):
	total = 0
	for n in a_list:
		total = total + 1
	return total


def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count


def my_count_1(a_list):
	count = 0
	for n in a_list:
		if n == 1:
			count = count + 1
	return count


def is_list_empty(a_list):
	if length(a_list) == 0:
		return True
	else:
		return False

def my_max(a_list):
	if is_list_empty(a_list):
		return None
	b = a_list[0]
	for n in a_list:
		if n > b:
			b = n
	return b


def get_filenames(a_dirname):
	list_of_files = os.listdir(a_dirname)
	all_files = []
	for file_name in list_of_files:
		full_path = os.path.join(a_dirname,file_name)
		if not os.path.isdir(full_path):
	  		all_files.append(full_path)
	return all_files
#os.path.join gives the right slash, when adding the directory path to the file name
#appending(=adding to the end of a list) 
#os.listdir(a_dirname) ist a function which we imported by --> import os

# [12, 34, [56, 67], 78] -> [12, 34, 56, 67, 78]

list_d = [16, 14, [3,4], 36]
def flatten(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				new_list.append(i)
		else:
			new_list.append(n)
	return new_list


def print_right(a_list_with_lists):
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i, end="")
			print("")
		else: 
			print(n)


def single_row_stars(number):
	for n in range(number):
		print("*", end="")


def row_stars_slashes(number):
	for n in range(number):
		if n % 2 == 0:
			print("*", end="")
		else:
			print("/", end="")


def single_row_of(number,string):
	for n in range(number):
		print(string, end="")


def square_of_stars(number):
	for n in range(number):
		print(number * "*")


def square_of_stars2(number):
	for n in range(number):
		for m in range(number):
			print("*", end="")
		print("")

	
def rectangle_of_stars(rows,cols):
	for n in range(rows):
		for m in range(cols):
			print("*", end="")
		print("")


def list_by_2(a_list):
	new_list = []
	for n in a_list:
		new_list.append(n * 2)
	print(new_list)

def create_grid(number):
	new_grid = []
	for row in range(number):
		new_sublist = []
		for column in range(number):
			new_sublist.append("-")
		new_grid.append(new_sublist)
	return new_grid
		