# This program helps build lists almost instantly. 
# Tasks as simple as copying multiple lines of data into a list of strings is now 2 keys away (Ctrl+V) and done.

list = []
print("""\nBelow are the list of functions and guidelines to follow:
\n\t1.)To add data to list keep pressing enter after each word.
\t2.)To print the resulting list enter '/print'.
\t3.)To clear the existing list enter '/clear'. 
\t4.)To exit the program enter '/quit'.""") #quit
while(True):
    a = str(input("\nEnter the data here ==> "))
    if a == "/print":
        try:
            print(list)
        except:
            print("\n========Finish========")
    elif a == "/clear":
        list.clear()
        print("\nThe list has been cleared!")
    elif a == "/quit":
        print("\n======== Thanks, Have a good day! ========")
        break
    else:
        list.append(a)