# TODO task 1

def calc_smallest_divisible(num_1: int, num_2: int) -> int:
    if num_1 <= 0 or num_2 <= 0:
        raise ValueError('Invalid input. Both numbers should be positive.')
    else:
        smallest_divisible = num_1
        while smallest_divisible % num_2 != 0:
            smallest_divisible += num_1
        return smallest_divisible


print(calc_smallest_divisible(5, 7))

# TODO task 2


