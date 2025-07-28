
# 1. List Creation using List Comprehension
# This code creates a list of squares of numbers from 1 to 10 using list comprehension

squares = [i**2 for i in range(1, 11)]
print("Squares from 1 to 10:", squares)

print("--------------------")

# 2. Filtering Even Numbers using List Comprehension
# # It generates a list of even numbers from 0 to 10
even_numbers = [num for num in range(11) if num % 2 == 0]
print("Even numbers from 0 to 10:", even_numbers)

print("--------------------")

# 3. Nested loops using List Comprehension
# This code creates a list of tuples representing pairs of numbers from two ranges
pairs = [(x,y) for x in range(3) for y in range(2)]
print("Pairs from two ranges:", pairs)