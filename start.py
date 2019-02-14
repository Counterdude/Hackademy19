import code
import pprint


# print("Greetings, travellers!")

# def hello(a_name):
# 	print("hello " + a_name)

# a, b = input("Please write your name, traveller 1! Then, press Enter. "), input("Please write your name, traveller 2! Then, press Enter. ") 

# code.hello2(a, b)

# code.print_right(code.list_d)

# code.single_row_stars(6)

# code.row_stars_slashes(6)

# code.single_row_of(3, "&/")

# num = int(input("give me a number:"))
# string = input("give me a string:")
# code.single_row_of(num, string)

# code.square_of_stars(4)
# code.square_of_stars(5)
# code.square_of_stars2(4)



code.rectangle_of_stars(3,6)

list_a = [1,3,5,8]
code.list_by_2(list_a)


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(code.create_grid(4)) 