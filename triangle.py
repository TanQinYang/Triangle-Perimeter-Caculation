import math
x1 = float(input("Enter x value for point 1: "))
y1 = float(input("Enter y value for point 1: "))
x2 = float(input("Enter x value for point 2: "))
y2 = float(input("Enter y value for point 2: "))
print("Point 3 set to (0,0)")
print("Distance between points 1 and 2:",str(math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))))
print("Distance between points 1 and 3:",str(math.sqrt(math.pow(x1,2) + math.pow(y1,2))))
print("Distance between points 2 and 3:",str(math.sqrt(math.pow(x2,2) + math.pow(y2,2))))
print("Perimeter of triangle:",str(math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2)) + math.sqrt(math.pow(x1,2) + math.pow(y1,2)) + math.sqrt(math.pow(x2,2) + math.pow(y2,2))))