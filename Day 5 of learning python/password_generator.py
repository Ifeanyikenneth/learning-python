import random

print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

# this is the easy level
password = ""

for character in range(1, nr_letters + 1): 
  random_character = random.choice(letters)
  password = password + random_character
  # print(password)

for character in range(1, nr_symbols + 1): 
  random_character = random.choice(symbols)
  password += random_character
  # print(password)


for character in range(1, nr_numbers + 1): 
  random_character = random.choice(numbers)
  password += random_character
  # print(password)


print(f"your password is: {password}")


password_list = list(password)
random.shuffle(password_list)


# print(password_list)
shuffled_password = ""
for each_value in password_list:
  shuffled_password += each_value

print(f"your shuffled password is: {shuffled_password}")


# for the hard level





# 14:46
# //Convert Password string to a List
# //Shuffle the List

# //Convert password back to a string











