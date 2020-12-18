import random


def play():
    user = input("'r' for rock 'p' for paper 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'You Win'

    return 'You Lost'


def is_win(player, opponent):

    if(player == 'r' and opponent == 's') or (player == 'r' and opponent == 's') \
            or (player == 'r' and opponent == 's'):
        return True


print(play())
