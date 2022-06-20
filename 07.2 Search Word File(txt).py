# This program prints the occurrence of a word from a txt file.

def main(): #Create sample binary file with fields if does not exist
    global f

    while True:
        global a
        a = f"Tomorrow Poem.txt"
        try:
            global f
            f = open(a, "r+")
            break
        except:
            print("\nPreparing program for first launch...\nCreating TXT file...\nWriting sample poem to TXT file...")
            with open(a, "w") as f:
                sample = 'Tomorrow I will start to be happy.\nThe morning will light up like a celebratory cigar.\nSunbeams sprawling on the lawn will set\ndew sparkling like a cut-glass tumbler of champagne.\nToday will end the worst phase of my life.\n\n\nI will put my shapeless days behind me,\nfencing off the past, as a golden rind\nof sand parts slipshod sea from solid land.\nIt is tomorrow I want to look back on, not today.\nTomorrow I start to be happy; today is almost yesterday.'
                f.write(sample); pass
main()

print(f"\nSearching from {a}\n")
content_str = f.read(); f.seek(0, 0); print(content_str)
content = f.readlines()
word = input('\nEnter the word to search: ')
count = pos = 0
loc = []

def filter(lis):
    global pos, count
    for line in lis:
        if word in line: count += 1
filter(content)
print(f"\nThe word '{word}' occurs {count} time(s).")