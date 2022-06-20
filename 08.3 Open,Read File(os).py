# This programs lists all text files available in a directory and lets the user view contents of that file.

from os import listdir

def main():
    direc = [i for i in listdir() if 'txt.' in i[-1:2:-1]]
    print("\nSelect a TXT file (number) to Open/Read:\n")
    for i, j in enumerate(direc): 
        print(f'\t{i} --> {j}')
    inp = int(input('\n=> '))
    iterate = True
    while iterate == True:
        try:
            f = open(direc[inp], 'r')
            print(f.read())
            iterate = False
            if input('\nWant to read another file? (y/n) : ').lower() == 'y':
                main()
            else:
                quit()

        except Exception:
            print("\nEnter a valid TXT file!")
main()