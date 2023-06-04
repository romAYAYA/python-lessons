# TODO task 1

# def calc_smallest_divisible(num_1: int, num_2: int) -> int:
#     if num_1 <= 0 or num_2 <= 0:
#         raise ValueError('Invalid input. Both numbers should be positive.')
#     else:
#         smallest_divisible = num_1
#         while smallest_divisible % num_2 != 0:
#             smallest_divisible += num_1
#         return smallest_divisible
#
#
# print(calc_smallest_divisible(7, 5))

# TODO task 2

# returns all lost elements

# def search_lost_element(check_cards_list: [int]) -> list:
#     lost_cards_list = []
#
#     for element in range(1, max(check_cards_list) + 1):
#         if element not in check_cards_list:
#             lost_cards_list.append(element)
#
#     return lost_cards_list


# first lost element search

# def search_lost_element(check_cards_list: [int]) -> int:
#     for element in range(1, max(check_cards_list) + 1):
#         if element not in check_cards_list:
#             return element
#
#     return "It's okay"
#
#
# print(search_lost_element([1, 2, 3, 5]))


# TODO task 3

# def sqrt(num: int) -> list:
#     res = []
#
#     for i in range(1, num):
#         if i ** 2 < num:
#             res.append(i ** 2)
#
#     return res
#
#
# print(sqrt(50))

# TODO task 4

# def calc(num_1: float, num_2: float, action: str) -> float | str:
#     match action:
#         case '+':
#             res = num_1 + num_2
#             return res
#         case '-':
#             res = num_1 - num_2
#             return res
#         case '*':
#             res = num_1 * num_2
#             return res
#         case '/':
#             if num_2 != 0:
#                 res = num_1 / num_2
#                 return round(res, 1)
#             else:
#                 return 'You should not do this :c'
#         case _:
#             return 'Invalid action'
#
#
# num_1_input = float(input('Enter first number: '))
# num_2_input = float(input('Enter second number: '))
# action_input = str(input('Enter an action (+, -, *, /): '))
#
# print(calc(num_1_input, num_2_input, action_input))

# TODO 5 task

def check_accessory(list_nums: list[int], check_nums: list[int]) -> bool:
    if not list_nums:
        return True
    elif list_nums[0] not in check_nums:
        return False
    else:
        return check_accessory(list_nums[1:], check_nums)


print(check_accessory([2, 2, 1, 2], [1, 2]))
print(check_accessory([2, 2, 3, 2], [1, 2]))
