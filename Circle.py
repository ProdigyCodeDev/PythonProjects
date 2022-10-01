import math

def area(r):
    return math.pi * r**2

def circumference(r):
    return math.pi * 2 * r

radius = float(input("Circle Radius:   "))

circle_area = area(radius)
circle_circumference = circumference(radius)

print('Area:  ' + str(circle_area))
print('Circumference:' + str(circle_circumference))