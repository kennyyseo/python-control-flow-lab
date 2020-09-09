# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term = 0
number_list = [1, 1]
while term == 0:
    print('term: 0 / number: 0')
    term += 1

while term == 1:
    print('term: 1 / number: 1')
    term += 1

while term == 2:
    print('term: 2 / number: 1')
    term += 1

while term < 50:
    number = number_list[-2] + number_list[-1]
    number_list.append(number)
    print(f'term: {term} / number: {number}')
    term += 1
