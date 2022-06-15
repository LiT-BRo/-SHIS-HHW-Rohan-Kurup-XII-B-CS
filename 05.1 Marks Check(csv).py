# Program to view Record of Marks scored by students in CSV format.

from csv import *

def chk(f):
    f.close()
    f = open("Marks.csv", "r+") #To refresh current db data 
    database = reader(f);print()
    database = list(database)
    [print(",".join(row)) for row in database]
def main(): #Create csv file with fields if does not exist
    global f
    while True:
        try:
            f = open("Marks.csv", "r+")
            break
        except:
            print("\nPreparing program for first launch...\nCreating CSV file...\nWriting sample fields to CSV file...")
            with open("Marks.csv", "w") as f:
                csv_w = writer(f)
                csv_w.writerows([['Name', 'Stream', 'Phy', 'Chem', 'Maths', 'Eng', 'Bio', 'Acc', 'Bus-Stu', 'Eco', 'His', 'Geo', 'Pol-Sci', 'CS', 'Psy', 'Socio', 'IP', 'A-Maths', 'PE', 'Paint'],['Raghav', 'science', '45', '43', '', '42', '34', '', '', '', '', '', '', '50', '', '', '', '', '', '']]) #Fields for csv
main()

while True:
    opt = input("\nWould you like to:\n\t1 ==> See the current database\n=> ").lower()
    if opt == "1":
        chk(f)