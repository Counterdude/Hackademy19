import random
import code

def setup_game(size, max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)


def get_empty_grid(number):
	new_grid = []
	for row in range(number):
		new_sublist = []
		for column in range(number):
			new_sublist.append("-")
		new_grid.append(new_sublist)
	return new_grid


def rand_alive():
    number = random.randint(1,2)
    if number == 1:
        return True
    else:
        return False


# l = len(a)

# for i in range(len(a)):
#     a[i] = "rrr"


def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if rand_alive() == True and remaining != 0:
                a_grid[r_i][c_i] = "x"
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = "-"
    return a_grid


def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i], end=" ")
        print("")


my_grid = code.create_grid(6)
my_grid = fill_grid_random(my_grid,5)
print_grid(my_grid)


list_a = [4,16,89,36,17]
list_b = [1,43, 67,3,9]

def is_duplicate_there(list_a,list_b):
    counter = 0
    for n in list_a:
        for m in list_b:
            if n == m:
                counter = counter + 1
    if counter !=0:
        return True
    else:
        return False 
                

is_duplicate_there(list_a,list_b)
