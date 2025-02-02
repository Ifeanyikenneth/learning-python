# # # # # # # # # name = int(input("which number do you want to check? "))

# # # # # # # # # if name % 2 == 0:
# # # # # # # # #   print("this is an even number.")

# # # # # # # # # else :
# # # # # # # # #   print("this is an old number.")


# # # # # # # # height = float(input("enter your height in m: "))
# # # # # # # # weight = float(input("enter your weight in kg: ")) 


# # # # # # # # add = round(weight / height ** 2) 


# # # # # # # # if  add < 18.5 :
# # # # # # # #   print("you are underweight.")

# # # # # # # # elif add < 25 :
# # # # # # # #   print("you are noraml weight.")

# # # # # # # # elif add < 30 :
# # # # # # # #   print("you are overweight.")

# # # # # # # # # elif add < 35 :
# # # # # # # # #   print("you are obese.")

# # # # # # # # # elif add > 30 :
# # # # # # # # #   print("you are cliniclaly obese.")


# # # # # # # # # year = int(input("what year do you want to check? "))

# # # # # # # # # if year % 4 == 0 :
# # # # # # # # #   print("leap year.")

# # # # # # # # # else :
# # # # # # # # #   print("not leap year.")


# # # # # # # # print("Welcome to python pizza deliveries!")
# # # # # # # # name1 = input("what size of pizza do you wants? S, M, or L ").lower()
# # # # # # # # name2 = input("do you want pepperoni? Y or N  ").lower()
# # # # # # # # name3 = input("do you want extra cheese? Y or N ").lower()

# # # # # # # # add = 0 

# # # # # # # # if name1 == "s":
# # # # # # # #   add += 15

# # # # # # # # if name1 == "m":
# # # # # # # #   add += 20

# # # # # # # # if name1 == "l":
# # # # # # # #   add += 25


# # # # # # # # if name2 == "y":
# # # # # # # #   if name1 == "s": 
# # # # # # # #     add += 2

# # # # # # # #   else:
# # # # # # # #     add += 3


# # # # # # # # if name3 == "y":
# # # # # # # #   add += 1


# # # # # # # # else :
# # # # # # # #   print(f"you final bill is ${add}")




# # # # # # # name1 = input("what is your name? \n").lower()
# # # # # # # name2 = input("what is thier name ? \n").lower()

# # # # # # # combine = name1 + name2

# # # # # # # t =combine.count("t")
# # # # # # # r =combine.count("r")
# # # # # # # u =combine.count("u")
# # # # # # # e =combine.count("e")

# # # # # # # true = t + r + u + e 

# # # # # # # l =combine.count("l")
# # # # # # # o =combine.count("o")
# # # # # # # v =combine.count("v")
# # # # # # # e =combine.count("e")

# # # # # # # love = l + o + v + e 

# # # # # # # add = int(str(love) + str(true))

# # # # # # # if add < 10 or add >90 :
# # # # # # #   print(f"your score is {add}, you go together like coke and mentos.")

# # # # # # # elif add >= 40 and add <=50 :
# # # # # # #   print(f"you score is {add}, you are alright together.")

# # # # # # # else :
# # # # # # #   print(f"your score is {add}")

# # # # # # # random_float = random.random()

# # # # # # # # print(random_float)
# # # # # # # import random 

# # # # # # # rands = random.randint(0,1)

# # # # # # # if rands == 0:
# # # # # # #   print("Heads")

# # # # # # # else :
# # # # # # #   print("Tails")

# # # # # # import random 



# # # # # # # user_choice = int(input("what do you chooose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# # # # # # # # print(combine = [user_choice])
 
# # # # # # # rock = '''____'''
# # # # # # # scissor = '''-'''
# # # # # # # paper = '''__'''




# # # # # # # combine = [rock ,scissor, paper]






# # # # # # computer_choice = random.randint(0, 2)

# # # # # # print(computer_choice) 
# # # # # # # print(combine[computer_choice])





# # # # # # if user_choice >=3 or user_choice < 0 :
# # # # # #   print("you typed an invalid number, you lose!") 
# # # # # # elif user_choice == 0 and computer_choice == 2 :
# # # # # #   print("You win!")
# # # # # # elif computer_choice > user_choice:
# # # # # #   print("you lose")
# # # # # # elif user_choice > computer_choice:
# # # # # #   print("you win!")
# # # # # # elif computer_choice == user_choice :
# # # # # #   print("It's a draw")



    
# # # # # student_height = input("input a value to run. ",).split()

# # # # # for n in range(0, len(student_height)):
# # # # #   student_height[n] = int(student_height[n])
# # # # # print(student_height)

# # # # # addition = 0

# # # # # for height in student_height:
# # # # #   addition += height
# # # # # print(addition)

# # # # # adding = 0 

# # # # # for student in student_height:
# # # # #   adding += 1
# # # # # print(adding)

# # # # # final = round(addition / adding)

# # # # # print(f"your final result is {final}")



# # # # # addition = 0 

# # # # # for summation in range(1,101):
# # # # #   if summation % 2 == 0:
# # # # #     addition += summation
# # # # # print(addition)
   

 
# # # # # adding  = 0 

# # # # # for number in range(2,101,2):
# # # # # #   adding += number
# # # # # # print(adding)


# # # # # for number in range(1, 101):
# # # # #   if number % 3 == 0 and number % 5 == 0:
# # # # #     print("FizzBuzz")
# # # # #   elif number % 3 == 0:
# # # # #     print("Fizz")
# # # # #   elif number % 5 == 0:
# # # # #     print("Buzz")
# # # # #   else:
# # # # #     print(number)








# # # # student_heights = input("input a value to run. ",).split()

# # # # for n in range(0, len(student_heights)):
# # # #   student_heights[n] = int(student_heights[n])
# # # # print(student_heights)


# # # # highest_value = student_heights[0]

# # # # for student_height in student_heights:
# # # #   if student_height > highest_value:
# # # #     highest_value = student_height
# # # # print(highest_value)
 

# # # # # using the lowest value

# # # # #it will get the first value in the list

# # # # # lowest_value = student_heights[0]

# # # # # for student_height in student_heights:
# # # # #   if student_height < lowest_value:
# # # # #    lowest_value = student_height
# # # # # print(lowest_value)





# # # # for student in range(1,101):
# # # #   if student % 3 == 0 and student % 5 == 0:
# # # #     print("fizzbuzz")
# # # #   elif student % 3 == 0:
# # # #     print("fizz")
# # # #   elif student % 5 == 0:
# # # #     print("buzz")
# # # #   else:
# # # #     print(student)


# # # password = ""

# # # for character in range(1, nr_letters + 1): 
# # #   random_character = random.choice(letters)
# # #   password = password + random_character
# # #   # print(password)

# # # for character in range(1, nr_symbols + 1): 
# # #   random_character = random.choice(symbols)
# # #   password += random_character
# # #   # print(password)


# # # for character in range(1, nr_numbers + 1): 
# # #   random_character = random.choice(numbers)
# # #   password += random_character
# # #   # print(password)


# # # print(password)
# # # # password_list = password.split()
# # # # random.shuffle(password_list)

# # # # password = str(password_list)

# # # # print(password)


# # import random

# # print("Welcome to the PyPassword Generator!")
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
# #             'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
# #            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# # nr_letters = int(input("How many letters would you like in your password? \n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like? \n"))


# # password = ""

# # for character in range(1, nr_letters + 1): 
# #   random_character = random.choice(letters)
# #   password = password + random_character
# #   # print(password)

# # for character in range(1, nr_symbols + 1): 
# #   random_character = random.choice(symbols)
# #   password += random_character
# #   # print(password)


# # for character in range(1, nr_numbers + 1): 
# #   random_character = random.choice(numbers)
# #   password += random_character
# #   # print(password)


# # print(password)
# # password_list = list(password) #password.split()

# # random.shuffle(password_list)
# # password12 = ""
# # for loop in password_list:
# #   password12 += loop
# # print(password12)







# def my_function():  
#   print("Hello + world")
#   print("How are you doing today hope all is alright over there.")
#   print("where is your dad")
#   print("i hope your are copying with your studies.")



# my_function()



# def student():
#   print("heloo")



# student


import random 

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

display = []
for d in range(len(chosen_word)):
  display += "_"
print(display)




# # print (chosen_word)
guess = input("Guess a letter. ").lower()


for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter 


print(display)


   
 


































