# getting random password
import passwordGenerator

print("Please provide the below content to generate random password::")
nr_letters = int(input("How many letters you need in your password: "))
nr_symbols = int(input("How many symbols you need in your password: "))
nr_numbers = int(input("How many numbers you need in your password: "))

new_password = passwordGenerator.random_password_generator(nr_letters, nr_symbols, nr_numbers)

print(f"Newly generated password :: {new_password}")