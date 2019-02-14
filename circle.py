import math

def circle_area(radius):
    A = math.pi * radius ** 2
    return A

input_radius = float(input("Please enter a radius, please "))


print(circle_area(input_radius))
