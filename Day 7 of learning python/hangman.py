world_list = ["baboon", "camel", "ardvard" ]

import random 

chosen_word = random.choice(world_list)
print(chosen_word)

display = []
for each_letter in range(len(chosen_word)):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower() 

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter


print(display)

