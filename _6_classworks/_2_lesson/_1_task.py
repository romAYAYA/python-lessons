name = input('Enter your name: ')
age = int(input('Enter your age: '))  # Convert age to integer
job = input('Enter your job: ')

print(f'Name: {name}, Age: {age}, Job: {job}')

if age > 18:
    print('You can drive a car!')
else:
    print('Get out of here, shket')
