# First of all make a list of dice emoji
# Generate a random number
# Compare dice value against previous value


import random
import os
#clearing the screen between rounds
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "social media platform",
        "country": "United States",
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "Country": "Portugal",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and Professional wrestler",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality Tv personality and businesswoman and Self-Made Billionaire",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "followers_count": 167,
        "description": "Reality Tv and businesswoman",
        "country": "United States",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 149,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Jenna Ortega",
        "follower_count": 234,
        "description": "An Actress",
        "country": "United States",
    },
]

# Display art
# Generate a random account from the game data
# Format the data into printable format
# Ask user for a guess
# Check if user is correct
# Get follower count of each account.
# use if statement to check if user is correct
# give user feedback on their guess.
# score keeping
# make the game repeatable.
# making the account at position B become the account at position A
# clear the screen between rounds


score = 0
game_should_continue = True
account_b = random.choice(data)


# make the game repeatable
while game_should_continue:

    # Dispaly art
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Format the data into printable format
    # account_name = account_a["name"]
    # account_description = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{"name"}, a {"description"}, from {"country"}")

    # ok lets say without calling out the accout_A and b and lets just have a particular def function for it
    def format_data(account):
        """format the account data into printable format."""
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_description}, from {account_country}"

    print(f"Compare A, {format_data(account_a)}.")
    print(f"Compare B, {format_data(account_b)}.")

    # Asking the user for a guess who has more follower.
    guess = input("Who has more follower? Type 'A' or 'B' ").lower()

    # Check if user is correct
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # use if statement to check if user is correct

    def check_answer(guess, a_followers, b_followers):
        """Take the user guess and the follower counts and returns if the got it right."""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    # giving user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong Current score: {score}")


