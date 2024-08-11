# write a function that will generate random password for given data.
# how many characters you need in your password
# how many symbols you need in your password
# how many numbers you need in your password

# example:
# user will select 10 characters or letters , 4 symbols and 5 numbers
# password will be : hfdj$%67@3(LKS2ye5

import random
import string


def random_password_generator(letters_num: int, symbols_num: int, numbers_num: int):
    letters = list(string.ascii_letters)
    symbols = ['(', ')', '$', '#', '&', "*", '@', '_']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # find which input value is greater than all other values.
    range_max = max(letters_num, symbols_num, numbers_num)

    selected_letters = []
    selected_symbols = []
    selected_numbers = []

    for letter in range(0, range_max):
        if letter < letters_num:
            selected_letters.append(random.choice(letters))
        if letter < symbols_num:
            selected_symbols.append(random.choice(symbols))
        if letter < numbers_num:
            selected_numbers.append(random.choice(numbers))

    new_password = selected_letters + selected_symbols + selected_numbers

    new_password = random.sample(new_password, len(new_password))

    generated_password = ""

    for one_char in new_password:
        generated_password += one_char

    return generated_password
