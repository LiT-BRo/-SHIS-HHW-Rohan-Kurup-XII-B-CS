# Tac-Tac-Toe now comes to Python, compete againt computer and win!

from random import choice
v_l = '|' #Vertical Line
h_l = '--' #Horizontal Line

def b_print():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    a1, b1, c1, a2, b2, c2, a3, b3, c3 = moves
    board = f"""
 {a1} {v_l} {b1} {v_l} {c1}
{h_l}{h_l}{h_l}{h_l}{h_l}{h_l}
 {a2} {v_l} {b2} {v_l} {c2}
{h_l}{h_l}{h_l}{h_l}{h_l}{h_l}
 {a3} {v_l} {b3} {v_l} {c3}\n"""
    print(board)

def eval(n): #Evaluate for wins
    iterate = True
    if (a1==b1==c1) or (a2==b2==c2) or (a3==b3==c3) or (a1==a2==a3) or (b1==b2==b3) or (c1==c2==c3) or (a1==b2==c3) or (a3==b2==c1):
        if n == "main": # With above criteria, player with last move can win the match
            print("Bot Wins!")
        else:
            print("Player Wins!")
        iterate = False
        inp = input("\nWant to try another round? (y/n): ").lower()
        if inp == 'y':
            prog_start()
        else: print("\nGood Game!")
    if iterate == True:
        if n == 'bot':
            bot()
        else: main()

def bot(): #Bot Move
    global used, board
    print("Bot choosing move...")
    pos = choice([i for i in moves if str(i).isnumeric()])
    moves[pos-1] = 'O'
    b_print()
    eval("main")

def main(): #User move
    global board
    pos = int(input("Enter number to mark: "))
    moves[pos-1] = 'X'
    b_print()
    eval("bot")

def prog_start(): #Initiator Also Restarter
    global moves
    moves = [i for i in range(1, 10)]
    b_print()
    main()

prog_start()