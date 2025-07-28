# 1. Square of even numbers from 1 to 10

square_of_even = [x**2 for x in range(1,11) if x % 2 == 0]

print("Square of even numbers from 1 to 10:", square_of_even)

print("--------------------------------------------------------")

# 2. Capitalize all words in a list
words = ["hello", "world", "python", "list", "comprehension"]
capitalized_words = [word.capitalize() for word in words]
print("Capitalized words:", capitalized_words)

# 3. Create a list of tuples with numbers and their squares
numbers_and_squares = [(x, x**2) for x in range(1, 11)]
print("Numbers and their squares:", numbers_and_squares)

# 4. Flatten a list of lists
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
print("--------------------------------------------------------")

# 5. Create a list of even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)

# 6. Sum of all numbers in a list using reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers in the list:", sum_of_numbers)