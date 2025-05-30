import random



EASY_LEVEL_TURNS = 10

HARD_LEVEL_TURNS = 5



# Function to check user's guess against the actual answer

def check_answer(guess, answer, turns):

    if guess > answer:

        print("Too high.")

        return turns - 1

    elif guess < answer:

        print("Too low.")

        return turns - 1

    else:

        print(f"You got it! The answer was {answer}.")



# Function to set difficulty level

def set_difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":

        return EASY_LEVEL_TURNS

    else:

        return HARD_LEVEL_TURNS



# Main game function

def game():

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    # print(f"Pssst, the correct answer is {answer}")  # Uncomment for debugging



    turns = set_difficulty()

    guess = 0



    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number.")



        # Let the user guess a number

        guess = int(input("Make a guess: "))



        # Check the guess and update the number of turns

        turns = check_answer(guess, answer, turns)



        if turns == 0:

            print("You've run out of guesses. You lose.")

            print(f"The correct answer was {answer}.")

            return

        elif guess != answer:

            print("Guess again.")



# Call the game function to start the game

game()