# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


greeting = print(
    'Enter the three lengths of a triangle')
l1 = int(input('a:'))
l2 = int(input('b:'))
l3 = int(input('c:'))

if l1 == l2 and l1 == l3 and l2 == l3:
    print(
        f'A triangle with sides of {l1}, {l2}, & {l3} is an equalateral triangle.')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print(
        f'A triangle with sides of {l1}, {l2}, & {l3} is a scalene triangle.')
else:
    print(
        f'A triangle with sides of {l1}, {l2}, & {l3} is an isoceles triangle.')
