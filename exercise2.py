import random


def random_check(luckynumber, guess):  # Takes the luckyNumber and the user's guess as an argument. Checks if the
    # luckyNumber has been guessed correctly. Print hints for the next guess and return True or False.
    """ Check if the luckynumber the same as the guessed number."""
    if range_check(guess):
        if luckynumber > guess:
            print("Go a little higher...")
            return False
        elif luckynumber < guess:
            print("Too high, go again...")
            return False
        else:
            print("Yay, You guessed correctly!")
            return True
    else:
        return False


def get_guess():  # This function gets a user's guess for the lucky number and returns it as an integer.
    """This function gets a user's guess for the lucky number and returns it as an integer."""
    user_guess = input()
    return int(user_guess)


def range_check(num):  # Checking if the passed number is within the range of allowed values.
    """Check if passed number is in allowed range."""
    if num in range(0, 101):
        return True
    else:
        print("Come on, enter a number within the specified range 0-100!")
        return False


def gameplay():  # This function draws the lucky number and starts the guessing procedure.
    """Draw a lucky number and start to guess."""
    lucky_number = random.randint(0, 100)
    success = False
    print("Let's begin... Please guess a number between 0 and 100:")
    # The magic happens: Draw a lucky_number between 0 and 100
    while not success:
        # The loop goes on as long as the user has not guessed correctly, then it stops.
        success = random_check(lucky_number, get_guess())


# Start the game
gameplay()
