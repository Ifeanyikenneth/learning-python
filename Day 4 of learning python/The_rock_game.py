import random 



user_choice = int(input("what do you chooose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# print(combine = [user_choice])
 
# rock = '''____'''
# scissor = '''-''' 

# combine = [rock ,scissor, paper]

computer_choice = random.randint(0, 2)

print(f"computer chose {computer_choice}") 
# print(combine[computer_choice])



if user_choice >=3 or user_choice < 0 :
  print("you typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2 :
  print("You win!")
elif computer_choice > user_choice:
  print("you lose")
elif user_choice > computer_choice:
  print("you win!")
elif computer_choice == user_choice :
  print("It's a draw")



    





