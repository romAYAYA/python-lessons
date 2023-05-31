import utils


def sort(a, b, c):
    tuple_a = (a, sum(a))
    tuple_b = (b, sum(b))
    tuple_c = (c, sum(c))

    tuple_res = sorted((tuple_a, tuple_b, tuple_c), key=lambda x: x[1])
    sorted_arrays = [item[0] for item in tuple_res]
    return sorted_arrays


a = [6, 2, 1]
b = [3, 4, 5]
c = [1, 2, 3]

print(sort(a, b, c))

res1 = utils.get_sum(1, 3)

print(res1)
