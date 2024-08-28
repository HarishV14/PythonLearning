number = 1

while number <= 3:
    print(number)
    number = number + 1

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')


#else clause
counter = 0

while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')


