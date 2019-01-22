# part1_multiples.py
# If we list all the natural numbers below 10 that
#  are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def calculate_sum_under (num, limit = 1000):
	return num * ((1+limit//num) * (limit//num) / 2)


print( calculate_sum(3) + calculate_sum(5) - calculate_sum(3*5) )