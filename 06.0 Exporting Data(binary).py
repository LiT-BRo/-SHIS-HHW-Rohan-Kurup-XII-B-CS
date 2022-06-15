# Binary files are the easiest to manage and utilize. Use pickle and convert data to a BAT file

from pickle import *

def export_b(data):
    global f
    f.close(); print(f"\nFollowing data will be exported: {data}\n\nExporting data...\nAppending data to current binary file...")
    with open("bin_file.dat", "rb") as f:
        old_data = load(f)
        if len(data) == 1: old_data.append(data)
        else: [old_data.append(i) for i in data]
    with open("bin_file.dat", "wb") as f:
        dump(old_data, f)
    print("Binary file successfully updated!\nExport complete.")
def main(): #Create sample binary file with fields if does not exist
    global f
    while True:
        try:
            f = open("bin_file.dat", "rb")
            break
        except:
            print("\nPreparing program for first launch...\nCreating Binary file...\nWriting sample data to binary file...")
            with open("bin_file.dat", "wb") as f:
                data = [{"Sidd":{"Maths":45, 'Phy':54, 'Chem':52}}, "Python is fun!", "a+b=c"]
                dump(data, f)
            continue
main()
data = []
while True:
    line = input("\nEnter a line of data to add to current binary file: ")
    data.append(line); inp = input("Want to add another line? (y/n): ").lower()
    if inp == "y": continue
    else: export_b(data); break