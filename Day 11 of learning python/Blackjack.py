# This is a game whereby the user picks card in form of number againts computer and it must not be over 21 or else you lose
# And the A are going to stand as 11 until te user goes over 21 then it can be represented as 1
# While the king and queen stands as 10 



import random

# hint 1
# create a deal_card function that use the list below to *return* a random card.
# 11 is the Ace
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# hint 2
# Deal the user and computer 2 cards each using deal_card()
# when you want to add a single item thats not a list we use the .append

user_cards = [] 
Computer_cards = [] 

for _ in range(2):
  user_cards.append(deal_card)
  Computer_cards.append(deal_card)
  # when you want to add an single item not a list to an existig list then you have to use .append
# hint 3
# Create a function called calculate_score() that take a list of cards as input.
# And return the score.
# LOok up the sum()function to help you do this
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 1 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)


  return sum(cards)

# hint 4
# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
# and return 0 inside the actual score. 0 will represent a blackjack in our game.

# hint 5 
# Inside calculate_score() check for an 1 (ace). if the score is already over 21, 
# Remove the 11 and replace it with a 1. You might need to look up append() and remove()


# call the calculate_score().if the computer or the user as a blakjack (0) or if 
# the user's score is over 21, then the game ends.
  

















