def beautiful_function(*nums, **keynums):
    beautiful_sum = 0
    for num in nums:
        if isinstance(num, int) or isinstance(num, float):
            beautiful_sum += num

    return beautiful_sum


def sum_of_all_integers(integers):
    if len(integers) == 0:
        return 0

    x = integers.pop()
    return x + sum_of_all_integers(integers)


def sum_of_even_integers(integers):
    if len(integers) == 0:
        return 0

    x = integers.pop()
    if x % 2 == 0:
        return x + sum_of_even_integers(integers)

    return sum_of_even_integers(integers)


def sum_of_odd_integers(integers):
    if len(integers) == 0:
        return 0

    x = integers.pop()
    if x % 2 == 1:
        return x + sum_of_odd_integers(integers)

    return sum_of_odd_integers(integers)


def is_integer(x):
    if isinstance(x, int):
        return x

    return 0
