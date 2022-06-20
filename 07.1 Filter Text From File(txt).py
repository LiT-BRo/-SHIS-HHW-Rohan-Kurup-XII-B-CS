# This program helps filter the content of a text file into sub parts such as Upper-Case, Vowels, Punctuations characters.

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

content = f.readlines()
cnt_upper=cnt_lower=cnt_consonents=cnt_vowels=cnt_punctuations = 0

class Str():
    def __init__(self, string):
        self.string = string
    def isonlyconsonent(self):
        cons = 'bcdfghjklmnpqrstvwxyz'
        condition = True
        for i in self.string:
            if i.lower() not in cons: 
                condition = False; break
        return condition
    def hasvowel(self):
        vowels = 'aeiou'
        condition = False
        for i in self.string:
            if i.lower() in vowels: 
                condition = True; break
        return condition
    def haspunctuation(self):
        symbols = ['!', '-', ',', '.', '?', '"', "'", ';']
        condition = False
        for i in self.string:
            if i in symbols: 
                condition = True; break
        return condition

def filter(lis):
    global cnt_upper,cnt_lower,cnt_consonents,cnt_vowels,cnt_punctuations
    for line in lis:
        for ele in line:
            if ele.isupper():               
                cnt_upper += 1
            if ele.islower():               
                cnt_lower += 1
            if Str(ele).isonlyconsonent():  
                cnt_consonents += 1
            if Str(ele).hasvowel():         
                cnt_vowels += 1
            if Str(ele).haspunctuation():   
                cnt_punctuations += 1
                
filter(content); f.seek(0, 0)

print(f"""Poem is as follows:\n\n{f.read()}\n\n
No. of Upper-Case Characters = {cnt_upper}
No. of Lower-Case Characters = {cnt_lower}
No. of Consonents = {cnt_consonents}
No. of Vowels = {cnt_vowels}
No. of Punctuations = {cnt_punctuations}""")