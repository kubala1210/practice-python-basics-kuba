def square_numbers(numbers):
    result = list(map(lambda x:x ** 2, numbers))
    return result

print(square_numbers([1, 2, 3, 4]))
