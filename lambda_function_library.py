# Lambda Functions

# This file contains a library of lambda functions that can be used in various contexts.


square = lambda x: x ** 2
print("Square of 2:", square(2))


reverse = lambda s: s[::-1]
print("Reverse of 'hello':", reverse("hello"))


filter_evens = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print("Even numbers in [1, 2, 3, 4, 5]:", filter_evens([1, 2, 3, 4, 5]))
