# Custom implementation of built-in higher-order functions like map, filter, and reduce
# map function is a higher-order function that applies a function to all items in an iterable
# filter function is a higher-order function that filters items in an iterable based on a condition
# reduce function is a higher-order function that reduces an iterable to a single value using a binary function

def custom_map(func, iterable):
    """Applies a function to all items in an iterable."""
    return [func(x) for x in iterable]

def custom_filter(func, iterable):
    """Filters items in an iterable based on a condition."""
    return [x for x in iterable if func(x)]

def custom_reduce(func, iterable, initial=None):
    """Reduces an iterable to a single value using a binary function."""
    result = iterable[0]
    for x in iterable[1:]:
        result = func(result, x)
    return result  

# Example usage of custom higher-order functions
if __name__ == "__main__":
    # Example for custom_map
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = custom_map(lambda x: x ** 2, numbers)
    print("Squared numbers:", squared_numbers)

    # Example for custom_filter
    even_numbers = custom_filter(lambda x: x % 2 == 0, numbers)
    print("Even numbers:", even_numbers)

    # Example for custom_reduce
    from functools import reduce
    sum_of_numbers = custom_reduce(lambda x, y: x + y, numbers)
    print("Sum of numbers:", sum_of_numbers)