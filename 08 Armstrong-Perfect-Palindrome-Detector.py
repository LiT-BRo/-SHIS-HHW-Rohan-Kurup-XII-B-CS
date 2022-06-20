# This is a program which detects if a number is a special number. Special numbers include Perfect Numbers, Palindromes, Narcissistic Numbers and Integers.

def armstrong(user_input):
    answer = 0
    units = len(str(user_input)) #Getting the length of the number for exponentiation
    for number in str(user_input): #Targetting each number individually
        answer += int(number)**units #Exponentiating the number at the active units place with the length of number to get the desired answer.
    if user_input == answer: return True #Number is Amrstrong
    else: return False #Number not Amrstrong

def perfect(user_input):
    answer = 0
    for divisor in range(1, user_input):
        if user_input % divisor == 0: answer += divisor
        else: pass
    if user_input == answer: return True #Number is perfect
    else: return False #Number not perfect

def palindrome(user_input):
    if len(str(user_input)) > 1:
        answer = int(str(user_input)[::-1])
        if user_input == answer: return True #Number is palindrome
        else: return False #Number not palindrome
    else: return False

def main():
    user_input = int(input("\nEnter a number (integer) to be analysed => "))
    if armstrong(user_input) == True: #0, 1, 153, 371, 407, 1634, 8208, 9474, 54748
        print(f"\nThe number '{user_input}' is an Armstrong Number")
    if perfect(user_input) == True: #6, 28, 496, 8128
        print(f"\nThe number '{user_input}' is a Perfect Number")
    if palindrome(user_input) == True: #Two digit or more
        print(f"\nThe number '{user_input}' is a Palindrome Number")
    if (armstrong(user_input) == False) and (perfect(user_input) == False) and (palindrome(user_input) == False):
        print(f"\nThe number '{user_input}' is just an Integer")
    main()
main()