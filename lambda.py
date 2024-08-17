# Question: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']

filtered_strings = list(filter(lambda s: len(s) > 5, strings))

print(filtered_strings)

# Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

from functools import reduce

numbers = [2, 4, 6, 8, 10]

doubled_numbers = list(map(lambda x: x * 2, numbers))

product = reduce(lambda x, y: x * y, doubled_numbers)

print(product)
