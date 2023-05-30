# TODO 1st decision

def count_cost(s: float, p: float, m: float) -> str:
    if m - (s + p) >= 0:
        return 'DA'
    else:
        return 'NET'


print('count_cost: ', count_cost(700, 800, 1500))


# TODO 2nd decision

def count_cost_2(s: float, p: float, m: float) -> str:
    return 'DA' if m - (s + p) >= 0 else 'NET'


print('count_cost2: ', count_cost_2(700, 800, 1000))

# TODO 3rd decision

count_cost_3 = lambda s, p, m: 'DA' if m - (s + p) >= 0 else 'NET'

print('count_cost3: ', count_cost_3(700, 800, 1500))

# TODO 4th decision

count_cost_4 = lambda s, p, m: 'DA' if m >= (s + p) else 'NET'

print('count_cost4: ', count_cost_4(500, 600, 2000))
