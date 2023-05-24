input_num_begin = int(input('Enter number a: '))
input_num_end = int(input('Enter number b: '))

sum_of_evens = 0

# for i in range(input_num_begin, input_num_end + 1):
#     if i % 2 == 0:
#         sum_of_evens += i
# print(sum_of_evens)

while input_num_begin <= input_num_end:
    if input_num_begin % 2 == 0:
        sum_of_evens += input_num_begin
    input_num_begin += 1
print(sum_of_evens)
