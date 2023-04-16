import math


def age_present():
    age = int(input('Age? '))
    return age


try:
    print(age_present())
except ValueError:
    print("Invalid Value!")
    print(age_present())

exit()

integers = 1, 2, 3, 4
print(mean(p=integers))

exit()


def welcome_message(call, system):
    print(f"hello, {call}")
    print(f"welcome to {system}")


print("Entry")
welcome_message("John", "Phyton 101")
welcome_message("Stefan", "Art class")
print("Please have a wonderful time!")
exit()

phone_number = input('Phone Number: ')
digits = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five'
}
output = []
for number in phone_number:
    output.append(digits.get(number, '!') + " ")
print(output)

Test = {
    "name": "Jesus Christ",
    "religion": "Buddhism"
}
print(Test.get("religion", "male"))
exit()
numbers = [1, 30, 9, 127, 35, 100, 42, 99]
max = numbers[1]
for variable in numbers:
    while variable > max:
        max = variable
print(max)

# for list grids
# [1 2 3
# 4 5 6
# 7 8 9]
y = [1, 3, 4, 5, 2, 3, 5, 7, 3, 1]
y.sort()
y.reverse()
print(y)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])
for rows in matrix:
    rows = matrix[1]
    for items in rows:
        items = rows[2]
print(items)
exit()

number = [2, 2, 2, 2, 5]
for variables in number:
    output = ''
    for x_count in range(variables):
        output += 'x'
    print(output)
exit()

# (x, y)
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')
exit()

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'total: {total}')
exit()
names = ['I', 'U', 'W', 'O', 'X', 'M', 'S', 'K']  # [] is for lists, () is for tuple(can't be changed)

for item in names:
    print(item)
y = 0
while y < len(names):
    print(names[y])
    y = y + 1
    exit()

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    win = int(input('guess: '))
    guess_count += 1
    if win == secret_number:
        print('you win! ')
        exit()
print('You Lose!')
exit()

g = 0
while g < 3:
    ans = int(input('guess: '))
    if ans == 9:
        print('Congrats!')
        exit()
    else:
        print('Try Again!')
    g = g + 1
exit()

i = 1
while i <= 100:
    print(i * 'penis_')
    i = i + 1

name = input('Name: ')
if len(name) <= 3:
    print('Mamamia!')
elif len(name) >= 20:
    print('Pizzaria!')
else:
    print('Perfecto!')

price = 1_000_000
print(f'The price of the house is {price}$.')


def question():
    credit = input('May_I_know_your_Credit_Score?_(G)ood/(B)ad ')
    if credit.upper() == 'G':
        down_g = 0.1 * price
        print(f'The down payment will be {down_g}$ ')
        exit()
    elif credit.upper() == 'B':
        down_b = 0.2 * price
        print(f'The down payment will be {down_b}$ ')
        exit()
    else:
        print('Please only answer with "G" or "B". ')
        question()
    exit()


question()

print(math.pi * 2.22)
print(math.ceil(math.pi * 2.22))
o = 3.14
print(round(o))
print(math.ceil(o))
print(- o)
print(abs(- o))
names = ['I', 'U', 'W', 'O', 'X', 'M', 'S', 'K']  # [] is for lists, () is for tuple(can't be changed)
names[3] = 'HI'
names.append('Y')
names.insert(3, 'B')
names.remove('I')
print('HI' in names)
print(names)
print(len(names))
for item in names:
    print(item)
y = 0
while y < len(names):
    print(names[y])
    y = y + 1

Numbers = range(6)  # 6 items start from 0, if put 5, 10, the numbers will be from 5 to 9, range(start, end, steps)
for item in Numbers:
    print(item)

i = 1
while i <= 100:
    print(i * 'penis_')
    i = i + 1

Weight = input('Weight: ')
Unit = input('(K)g or (L)bs: ')
if Unit.upper() == 'K':
    print('Weight in Lbs: ' + str(float(Weight) * 2.2) + 'Lbs')
elif Unit.upper() == 'L':
    print('Weight in Kg: ' + str(float(Weight) / 2.2) + 'Kg')

# exponentation
# multiplication and subtraction
# addition and subtraction

number = (9, 0, 8, 1)
print(number)

# items covered by bracket is a tuple
# tuple is an imutable item hence cannot be changed by other lines

