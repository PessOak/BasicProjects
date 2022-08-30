import random

def play():
    user = input("What will you choose? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Oops... it's a tie."
    
    if is_win(user, computer):
        return "Yesss! You won !! :D"

    return "Ouch... You lose!"

def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())