# Same in theory to the Number Game but there's more at stake now!
# Guess the random Alphabet prompted, lesser the tries the better...

from random import randint

def rand_alphabet():
    global alpha, count
    alpha = randint(65, 90)
    count = 0
rand_alphabet()
def eval(alpha, guess):
    global count
    count += 1
    if alpha-guess > 0:
        if alpha-guess > 1:
            print("Too low!")
        else: print("Very close!")
        main("\nGuess higher: ")
    elif alpha-guess < 0:
        if alpha-guess < -1:
            print("Too high!")
        else: print("Very close!")
        main("\nGuess lower: ")
    elif alpha-guess == 0:
        print(f"Yay! You guessed the number in {count} tries...")
        inp = input("\nWant to try another game? (y/n): ").lower()
        if inp == 'y':
            main(n=True)
        else: print("\nGood Game!")
count = 0
def main(string="\nGuess an alphabet b/w (A - Z) : ", n=False):
    if n:
        rand_alphabet()
    guess = ord(input(string).upper())
    eval(alpha, guess)
main()