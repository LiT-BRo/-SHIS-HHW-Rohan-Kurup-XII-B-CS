# This is a Factorial Finder but implemented in 2 different approaches.
# First method prints a series of factorials until 'n'
# Second method prints a direct answer.

def fact_s(n):
    from math import factorial
    for i in range(n+1):
        print(f'factorial of {n} is = {factorial(i)}')

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def main():
    n = int(input('\nInput the number to find factorial for/upto: '))
    inp = int(input("""Would you like to :
\t1 ==> Get Series of factorial of upto 'n' numbers
\t2 ==> Get the factorial of 'n' number\n=> """))
    
    if inp == 1:
        fact_s(n)
    elif inp == 2:
        fact(n)
        print(f'factorial of {n} is = {fact(n)}')
    main()
main()