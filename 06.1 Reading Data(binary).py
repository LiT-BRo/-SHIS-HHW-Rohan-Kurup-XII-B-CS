# This is a program to read data pickled into a binary file.

from pickle import *

def print_b(f):
    f.close()
    with open("bin_file.dat", "rb") as f:
        content = load(f)
        print(f"\n{content}")

def main(): #Create sample binary file with fields if does not exist
    global f

    while True:
        try:
            f = open("bin_file.dat", "rb")
            break

        except:
            print("""\nPreparing program for first launch...
Creating Binary file...\nWriting sample data to binary file...""")

            with open("bin_file.dat", "wb") as f:
                data = [
                    {"Sidd":{"Maths":45, 'Phy':54, 'Chem':52}}, 
                    "Python is fun!", 
                    "a+b=c"
                    ]
                dump(data, f)
            continue
main()

inp = input("\nTo print data from binary file, enter 'print': ").lower()
if inp == "print":
    print_b(f)