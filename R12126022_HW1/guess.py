import random
status  = ["scissors", "rock", "paper"]

def figure_guess():
    return random.choice(status)

def guess_print():
    print("This is print from guess_print.")