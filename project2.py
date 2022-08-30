import random

def guess_me(x):
    random_number = random.randint(1, x)
    guess_me = 0
    while guess_me != random_number:
        guess_me = int(input(f"Come forward, take a guess between 1 and {x}: "))
        if guess_me < random_number:
            print("Sorry, too low... Try again ;)")
        elif guess_me > random_number:
            print("Oops... too high! :( go again!")
    print(f"Yeeaah!! Congratz, you did it! You've guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or high, because low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yeeaahh, the computer guessed the number {guess} correctly! You are a smart machine aren't you!?")        

computer_guess(1000)  
#guess_me(1000)