#Written by Shiven Desai
#This program calculates the sum of a series of numbers entered by the user
MAX = 5
total = 0.0
print('This program calculates the sum of')
print(f'{MAX} numbers you will enter.')
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
    total1 = total/5
    print(f'The total sum is {total}.')
    print(f'The average is {total1}.')