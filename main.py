import random

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#size is 52 for letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#10
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#9

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters do you want your password to be? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))
website_name = input("What is the name of website this password created for? \n")

f = open("text.txt", "a")
numbers_for_letters = nr_letters - nr_symbols - nr_numbers
password = ""
all = [letters, numbers, symbols]
while len(password) != nr_letters:
    number = random.randint(0,2)
    if number == 0 and numbers_for_letters !=0:
        sub_number = random.randint(0,51)
        password += all[number][sub_number]
        numbers_for_letters -= 1
    if number == 1 and nr_numbers !=0:
        sub_number = random.randint(0, 9)
        password += all[number][sub_number]
        nr_numbers -= 1
    if number == 2 and nr_symbols != 0:
        sub_number = random.randint(0, 8)
        password += all[number][sub_number]
        nr_symbols -= 1


print(f"Your password for {website_name} is, {password}")
f.write(website_name + ": ")
f.write(password + "\n")
f.close()

"""
random.choice kullanılarak yapılan çözüm
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")




"""