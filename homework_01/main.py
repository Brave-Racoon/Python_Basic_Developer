"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    nums_list = []
    for en in nums:
        nums_list.append(en ** 2)
    return nums_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    # for ex. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def filter_numbers(nums, mold):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if mold == ODD:
        return list(filter(lambda x: (x % 2 != 0), nums))
    if mold == EVEN:
        return list(filter(lambda x: (x % 2 == 0), nums))
    if mold == PRIME:
        return list(filter(lambda x: (is_prime(x)), nums))


# print(power_numbers(1, 2, 5, 7))
# print(is_prime(42))
# print(filter_numbers([1, 2, 3], ODD))
# print(filter_numbers([2, 3, 4, 5], ODD))
# print(filter_numbers([1, 2, 3], EVEN))
# print(filter_numbers([2, 3, 4, 5], EVEN))
# print(filter_numbers([2, 3, 4, 7, 0, 13, 17, 12, 23, 29], EVEN))
