# This program aggregates percentage quickly followed by inputs for UTs And Term-lys

def progres(): #program-reset function
    rel = str(input("\nWould you like to try again? (y/n) => "))
    if rel == "y":
        main()
    elif rel == "n":
        exit()
    else: #Debugged to avoid errors
        print(" ")
        progres()

def main():
    iterate = True
    while iterate == True:
        p1 = float(input("\nEnter marks scored in Weekly-Test 1 (Out of 30) => "))
        if p1 >= 0 and p1 <= 31:
            while iterate == True:
                p2 = float(input("Enter marks scored in Weekly-Test 2 (Out of 30) => "))
                if p2 >= 0 and p2 <= 30:
                    while iterate == True:
                        t1 = float(input("Enter marks scored in Terminal-Exam (Out of 100) => "))
                        if t1 >= 0 and t1 <= 100:
                            res = ((p1 + p2)/3)+((t1*4)/5)
                            print("\nThe Final Aggregate result =", str(round(res, 2))+"%")
                            iterate = False
                        else: 
                            continue
                else: 
                    continue
        else: 
            continue
    progres()
main()