# Simulate a dice.
# Return a random number from 1 to 6 

from random import *
from time import sleep

inp = input("\nTo roll the dice, enter 'r' => ")
while inp != "s":
    if inp == 'r':
        no = randrange(1, 7)
        print("\nRolling", end="")
        for i in range(3):
            print('.', end='')
            sleep(0.5)
        if no == 6:
            print(f" Wow! {no}")
        elif no == 1:
            print(f" Oh no! {no}")
        else:
            print(f" {no}")
    sleep(0.7)
    inp = input("\nWant to roll again? enter 'r'. To stop, enter 's' => ")