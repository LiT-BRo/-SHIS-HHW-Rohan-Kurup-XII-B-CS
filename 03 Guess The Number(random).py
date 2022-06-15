# Guess the random prompted. Lesser the tries required, better you are! ;)

from random import randint

def rand_num():
    global num, count
    num = randint(0, 9)
    count = 0
rand_num()

def eval(num, guess):
    global count
    count += 1
    if num-guess > 0:
        if num-guess > 1:
            print("Too low!")
        else:
            print("Very close!")
        main("\nGuess higher: ")
    elif num-guess < 0:
        if num-guess < -1:
            print("Too high!")
        else:
            print("Very close!")
        main("\nGuess lower: ")
    elif num-guess == 0:
        print(f"Yay! You guessed the number in {count} tries...")
        inp = input("\nWant to try another game? (y/n): ").lower()
        if inp == 'y':
            main(n=True)
        else: print("\nGood Game!")

count = 0
def main(string="\nGuess a number b/w (0 - 9) : ", n=False):
    if n:
        rand_num()
    guess = int(input(string))
    eval(num, guess)

main()