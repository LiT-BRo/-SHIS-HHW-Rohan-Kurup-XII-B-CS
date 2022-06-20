# A simple Math Calculator but with advanced functions.

def progres(): #program-reset function
    rel = str(input("\nWould you like to try again? (y/n) => "))
    if rel == "y":
         mainp()
    elif rel == "n": 
        exit()

def sq(a): ##Advanced-Calc
    print("The square of", a, "=", a**2)
def sqr(a):
    print("The square-root of", a, "=", a**0.5)
def fac(a):
    from math import factorial
    print(f"The factorial of {a} is = {factorial(a)}")
    
def mainp():
    uinp = str(input("""\nBelow are the advanced calculators available:
\tSquare       --> a
\tSq.Root      --> b
\tFactorial    --> c
\nSelect from above the prefered operation => """))

    if uinp in ['a', 'b', 'c']:
        a = int(input("\nEnter the number => "))
        if uinp == "a":
             sq(a)
        elif uinp == "b": 
            sqr(a)
        elif uinp == "c": 
            fac(a)
    else: mainp()
    progres()
    
mainp()