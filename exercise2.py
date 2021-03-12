import random


def random_check(rand):
    guess = get_guess()
    if rand > guess:
        print("Go a little higher...")
        return False
    elif rand < guess:
        print("Too high, go again...")
        return False
    else:
        print("Yay, You guessed correctly!")
        return True


def get_guess():
    user_guess = input("Please guess a number between 0 and 100: ")
    return int(user_guess)


luckyNumber = random.randint(0, 100)
success = False
while not success:
    success = random_check(luckyNumber)
