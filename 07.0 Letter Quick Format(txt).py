# With the help of a pre-set format for a letter, this tool offers a great saving of time 
# Entering just the valid details such as the name of recipient, subject, sender's name, etc. the letter is complete within seconds.
 
from datetime import datetime
letter = """<|DATE|>\n
Sir/Madam\n
Subject: <|SUBJECT|>\n
Greetings from Ro's Coding Experiment House! I am very pleased to inform that you have been selected.\n\n
Regards,
<|USER|>
<|DESIGNATION|>""" #Multi-line strings are easier to format.

content = {
    "<|USER|>"         :"\nEnter your name => ",
    "<|SUBJECT|>"      :"\nEnter the subject => ",
    "<|DESIGNATION|>"  :"\nEnter your designation => "}

for a in content:
    letter = letter.replace(a, input(content[a])) #We are updating the value of letter with each variable at a time.
date = datetime.now().strftime('%B %d, %Y')
letter = letter.replace("<|DATE|>", date)

with open("Letter Format.txt", "w") as f:
    f.write(letter)
    print("Exported letter as 'Letter Format.txt'")