# A program to input marks scored for children of class XII of all streams

from csv import *

def ety():
    global f
    name = input("\nEnter the name: ")
    phy=chem=bio=maths=acc=eco=his=geo=pol=eng=cs=bus=psy=socio=ip=a_math=pe=paint=""
    while True:
        stream = input("Select the stream (Science, Commerce, Humanities): ").lower()
        if stream == "science":
            side_stream = input("Medical (M) or Non-Medical (NM): ").lower()
            phy = input("Enter marks in physics: ")
            chem = input("Enter marks in chemistry: ")
            if side_stream == "medical" or side_stream == "m":
                bio = input("Enter marks in biology: ")
            else: maths = input("Enter the marks in mathematics: ")
        elif stream == "commerce":
            acc = input("Enter marks in accountancy: ")
            bus = input("Enter marks in business studies: ")
            eco = input("Enter marks in economics: ")
        elif stream == "humanities":
            his = input("Enter the marks in history: ")
            geo = input("Enter the marks in geography: ")
            pol = input("Enter the marks in political science: ")
        else: print("Choose a valid option please..."); continue
        eng = input("Enter the marks in english: ")
        while True:
            opt = input("Choose optional subject: CS, Psy, Socio, IP, Maths, PE, Paint: ").lower()
            if opt == "cs":
                cs = input("Enter marks in CS: ")
            elif opt == "psy":
                psy = input("Enter marks in psychology: ")
            elif opt == "socio":
                socio = input("Enter marks in sociology: ")
            elif opt == "ip":
                ip = input("Enter marks in IP: ")
            elif opt == "maths":
                a_math = input("Enter marks in maths: ")
            elif opt == "pe":
                pe = input("Enter marks in PE: ")
            else: paint = input("Enter marks in paint: ")
            re = input("Add another addtional subject? (y/n): ").lower()
            if re == "y": continue
            else: break
        break
    row = [name, stream, phy, chem, maths, eng, bio, acc, bus, eco, his, geo, pol, cs, psy, socio, ip, a_math, pe, paint]
    print(f"\n{row}")
    csv_w = writer(f)
    csv_w.writerow(row)
    print("\nRow added to file 'Marks.csv'")

def main(): #Create csv file with fields if does not exist
    global f
    while True:
        try:
            f = open("Marks.csv", "r+"); break
        except:
            print("\nPreparing program for first launch...\nCreating CSV file...\nWriting sample fields to CSV file...")
            with open("Marks.csv", "w") as f:
                csv_w = writer(f)
                csv_w.writerows([['Name', 'Stream', 'Phy', 'Chem', 'Maths', 'Eng', 'Bio', 'Acc', 'Bus-Stu', 'Eco', 'His', 'Geo', 'Pol-Sci', 'CS', 'Psy', 'Socio', 'IP', 'A-Maths', 'PE', 'Paint'],['Raghav', 'science', '45', '43', '', '42', '34', '', '', '', '', '', '', '50', '', '', '', '', '', '']]) #Fields for csv
main()

while True:
    opt = input("\nWould you like to:\n\t1 ==> Make an entry for a child\n=> ").lower()
    if opt == "1":
        ety()