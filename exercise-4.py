# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:

tri_lengths = input("Please enter the three lengths of a triangle (a, b, c - one at a time - press Enter to start):")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

x_str = str(x)
y_str = str(y)
z_str = str(z)

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
if x == y == z:
    print ("A triangle with sides of " + x_str + y_str + z_str + " is an Equilateral Triangle")
elif x == y or y == z or x == z:
    print ("A triangle with sides of " + x_str + y_str + z_str + " is an Isosceles Triangle")
else:
    print ("A triangle with sides of " + x_str + y_str + z_str + " is a Scalene Triangle")


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

