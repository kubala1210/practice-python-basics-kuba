def square_numbers(numbers):
    result = map(lambda x:x**x, numbers)
    return result

print(square_numbers([1, 2, 3, 4])) 