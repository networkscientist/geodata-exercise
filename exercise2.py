import random


def random_check(rand, guess):  # Takes the luckyNumber and the user's guess as an argument. Checks if the luckyNumber
    # has been guessed correctly. Print hints for the next guess and return True or False.
    """Takes the luckyNumber and the user's guess as an argument. Checks if the luckyNumber has been guessed
    correctly. Print hints for the next guess and return True or False. """
    if guess in range(0, 101):
        if rand > guess:
            print("Go a little higher...")
            return False
        elif rand < guess:
            print("Too high, go again...")
            return False
        else:
            print("Yay, You guessed correctly!")
            return True
    else:
        print("Come on, enter a number within the specified range 0-100!")
        return False


def get_guess():  # This function gets a user's guess for the lucky number and returns it as an integer.
    """This function gets a user's guess for the lucky number and returns it as an integer."""
    user_guess = input("Please guess a number between 0 and 100: ")
    return int(user_guess)


# The magic happens: Draw a luckyNumber between 0 and 100
luckyNumber = random.randint(0, 100)
success = False
# The loop goes on as long as the user has not guessed correctly, the it stops.
while not success:
    success = random_check(luckyNumber, get_guess())
