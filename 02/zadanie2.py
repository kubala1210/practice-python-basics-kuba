# Zadanie 2

for x in range(1, 21):
    if x % 3 == 0:
        print(f"Liczba {x} jest podzielna przez 3")
    # else:
    #     print(f"Liczba {x} nie jest podzielna przez 3")


def square_numbers(numbers):
    result = list(map(lambda x: x ** 2, numbers))
    return result


print(square_numbers([1, 2, 3, 4]))
