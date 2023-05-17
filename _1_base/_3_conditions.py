# TODO условный оператор if-else

bool_condition1 = False

if bool_condition1:
    print('True 1')
else:
    print('False 2')
    print('Hi there')

value = 40

if value > 100:
    print('True 3 1')
elif value > 50:
    print('True 3 2')
elif value > 39:
    print('True 3 3')

fruit = 'apple'

if fruit == 'apple':
    print('You will die')
elif fruit == 'banana':
    print('OKay, you wont die today')
else:
    print('What is that?')

# [] - False, [''] - True, '' - False, 1 - True, 0 - False

# TODO условный оператор math-case

light = 'green'

match light:
    case 'red':
        print('Stop')
    case 'yellow':
        print('Proceed with caution')
    case 'green':
        print('Go')


# TODO тернарный оператор

a = 10
b = 20

res = ''
if a > b:
    res = 'True'
else:
    res = 'False'

print(res)

res2 = 'True' if a > b else 'False'
print(res2)