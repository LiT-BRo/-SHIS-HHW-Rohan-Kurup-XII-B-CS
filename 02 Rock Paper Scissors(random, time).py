#The classic game brought back to life with python. Compete with the computer and win!

from random import *
from time import sleep

opt = {'r':'Rock', 'p':'Paper', 's':'Scissors'}

def bot():
        global opt
        move = choice(['r', 'p', 's'])
        return opt[move]
def evaluate(bot_move, user_move):
    if (bot_move == "Rock" and user_move == "Paper") or (bot_move == "Paper" and user_move == "Scissors") or (bot_move == "Scissors" and user_move == "Rock"):
        return 1
    elif bot_move == user_move:
        return 2
    else: return 0
sleep(0.5)
while True:
    print("\nBot is choosing a move", end="")
    for i in range(3):
        print('.', end='')
        sleep(0.2)
    bot_move = bot(); print()
    for i in range(3, 0, -1):
        print(i, end=". ")
        sleep(1)
    user_move = opt[input(f"\nChoose your move {opt} => ")]
    evalNum = evaluate(bot_move,user_move)
    if bot_move == "Scissors": #improved asthetics (\t'Scissors' caused spacing trouble)
        user_move = "\b"*8+user_move
        print(user_move)
    print(f"""\n\tRobot\t\t\t\tHuman
\t\t\tV/S
\t{bot_move}\t\t\t\t{user_move}""")
    if evalNum == 1:
        sleep(2); print("\nYay! You Won!")
    elif evalNum == 2:
        sleep(2); print("\nPhew! A tie.")
    else:
        sleep(2); print("\nOh no! You Lost...")
    inp = input("\nWant to try another round? Yes(y)/No(n): ")
    if inp == 'y':
        continue
    else:
        print("\nGood Game!"); break
