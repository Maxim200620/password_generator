import random
import sys

# Entering data for the password / Ввод данных для пароля
long = int(input('Length of the password '))
if long <= 0:
    print("please don't repeat it again")
    sys.exit()

character = int(input('Use of letters (1 - big, 2 - small, 3 - all, 4 - none) '))
if character > 4:
    print("please don't repeat it again")
    sys.exit()

special_token = str(input('Use special characters (y / n) '))
if special_token == 'Y' or special_token == 'н' or special_token == 'Н' or special_token == 'y':
    special_token = 'y'
elif special_token == 'N' or special_token == 'т' or special_token == 'Т' or special_token == 'n':
    special_token = 'n'
else:
    print("please don't repeat it again")
    sys.exit()

number = str(input('Use numbers (y / n) '))
if number == 'Y' or number == 'н' or number == 'Н' or number == 'y':
    number = 'y'
elif number == 'N' or number == 'т' or number == 'Т' or number == 'n':
    number = 'n'
else:
    print("please don't repeat it again")
    sys.exit()

# creating dictionary / создание словаря
if character == 1:
    character_line = sum(1 for line in open('Alphabet_big.txt', 'r'))
    A_character = {}
    with open("Alphabet_big.txt") as file:
        key = 1
        for line in file:
            value = line.split()
            A_character[key] = value
            key = int(key) + 1
elif character == 2:
    character_line = sum(1 for line in open('Alphabet_small.txt', 'r'))
    A_character = {}
    with open("Alphabet_small.txt") as file:
        key = 1
        for line in file:
            value = line.split()
            A_character[key] = value
            key = int(key) + 1
elif character == 3:
    character_line = sum(1 for line in open('Alphabet_all.txt', 'r'))
    A_character = {}
    with open("Alphabet_all.txt") as file:
        key = 1
        for line in file:
            value = line.split()
            A_character[key] = value
            key = int(key) + 1
if special_token == 'y':
    special_token_line = sum(1 for line in open('Alphabet_special_token.txt', 'r'))
    A_special_token = {}
    with open("Alphabet_special_token.txt") as file:
        key = 1
        for line in file:
            value = line.split()
            A_special_token[key] = value
            key = int(key) + 1
elif special_token == 'n':
    special_token = 0

if number == 'n':
    number = 0
# creating password / создание пароля
password = ''
while long > 0:
    if character != 4 and character != 0:
        character = 1
    elif character == 4 or character == 0:
        character = 0

    if special_token != 0:
        special_token = 2
    else:
        special_token = 0

    if number != 0:
        number = 3
    else:
        number = 0
    pas = ''
    if character == 0 and special_token == 0 and number == 0:
        print("please don't repeat it again")
        sys.exit()
    elif character == 1 and special_token == 2 and number == 3:
        stage = random.randint(1, 3)
        if stage == character:
            a = random.randint(1, int(character_line))
            pas = A_character[a]
        elif stage == special_token:
            a = random.randint(1, int(special_token_line))
            pas = A_special_token[a]
        elif stage == number:
            a = random.randint(1, 9)
            pas = a
    elif character == 1 and special_token == 2 and number == 0:
        stage = random.randint(1, 2)
        if stage == character:
            a = random.randint(1, int(character_line))
            pas = A_character[a]
        elif stage == special_token:
            a = random.randint(1, int(special_token_line))
            pas = A_special_token[a]
    elif character == 0 and special_token == 2 and number == 3:
        stage = random.randint(2, 3)
        if stage == number:
            a = random.randint(1, 9)
            pas = a
        elif stage == special_token:
            a = random.randint(1, int(special_token_line))
            pas = A_special_token[a]
    elif character == 1 and special_token == 0 and number == 3:
        stage = random.randint(1, 2)
        if stage == 2 and number == 3:
            a = random.randint(1, 9)
            pas = a
        elif stage == character:
            a = random.randint(1, int(character_line))
            pas = A_character[a]
    elif character == 1 and special_token == 0 and number == 0:
        a = random.randint(1, int(character_line))
        pas = A_character[a]
    elif character == 0 and special_token == 2 and number == 0:
        a = random.randint(1, int(special_token_line))
        pas = A_special_token[a]
    elif character == 0 and special_token == 0 and number == 3:
        a = random.randint(1, 9)
        pas = a
    password += str(pas)
    long = int(long) - int(1)
password = password.replace("'", "")
password = password.replace("]", "")
password = password.replace("[", "")
print(password)