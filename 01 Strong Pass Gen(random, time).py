from random import *
from time import sleep

alpha = [chr(i) for i in range(97, 123)]
def ret_alpha(): #return alphabet
    return choice(alpha)
def ret_alpha_cap():
    return ret_alpha().upper()
def ret_num():
    return str(choice(range(10)))
def ret_sym():
    sym = [ '!', '@', '#', '$', '&']
    return choice(sym)
def main():
    global passw
    cases = {'0':ret_alpha(), '1':ret_alpha_cap(), '2':ret_num(), '3':ret_sym()}
    rn = randrange(4) #rn = random_num
    passw += cases[str(rn)]
passw = ""
while True:
    num = int(input("\nEnter the length of password (n>=8) : "))
    if num < 8:
        print("\nPlease enter a valid number.")
    else:
        break
sleep(0.5)
print("\nGenerating a strong password", end="")
for i in range(3):
    sleep(0.5)
    print('.', end='')
sleep(0.5)
[main() for i in range(num)]
print("\n\nGenerated!", end=" "); sleep(0.5)
print(f"{passw}\n")