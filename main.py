# This  a tic tac toe game written in python.
import os
squares = [None,None,None,None,None,None,None,None,None]
player1 = 'X'
player2='O'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def draw(squares):
	count=1
	#squares=[None,None,None,None,None,None,None,None,None]
	for square in squares:
		if count<3:
			if not square:
				print("|_",end="")
			elif square==1:
				print("|X",end="")
			elif square==2:
				print("|O",end="")
			count+=1
		else:
			if not square:
				print("|_|")
			elif square==1:
				print("|X|")
			elif square==2:
				print("|O|")
			count=1

def tictac():
    count=1
    for square in squares:
        if not square:
            if count<3:
               print("|_",end="")
               count+=1
            else:
                print("|_|")
                count=1
        elif square==1:
            if count<3:
               print(f"|{player1}",end="")
               count+=1
            else:
                print(f"|{player1}|")
                count=1
        elif square==2:
            if count<3:
               print(f"|{player2}",end="")
               count+=1
            else:
                print(f"|{player2}|")
                count=1
def isEmpty(sqr):
    return squares[sqr]
def player1_won()->bool:
    if squares[0] == squares[1] == squares[2]  == 1 or \
        squares[3] == squares[4] == squares[5]  == 1 or \
        squares[6] == squares[7] == squares[8]  == 1 or \
        squares[0] == squares[3] == squares[6]  == 1 or \
        squares[1] == squares[4] == squares[7]  == 1 or \
        squares[2] == squares[5] == squares[8]  == 1 or \
        squares[2] == squares[4] == squares[6]  == 1 or \
        squares[0] == squares[4] == squares[8]  == 1:
        return True
    else:
        return False
def player2_won()->bool:
    if squares[0] == squares[1] == squares[2]  == 2 or \
        squares[3] == squares[4] == squares[5]  == 2 or \
        squares[6] == squares[7] == squares[8]  == 2 or \
        squares[0] == squares[3] == squares[6]  == 2 or \
        squares[1] == squares[4] == squares[7]  == 2 or \
        squares[2] == squares[5] == squares[8]  == 2 or \
        squares[2] == squares[4] == squares[6]  == 2 or \
        squares[0] == squares[4] == squares[8]  == 2:
        return True
    else:
        return False
def isOver(): 
    if  player1_won():
         tictac()
         print("Player1 won")
         exit()
    elif player2_won():   
         tictac()
         print("Player2 won")
         exit()
    elif all(squares):
        print("All turns are taken.")
        tictac()
        exit()
   
def turn():
    cur_turn = "Player1"
    sq=1000
    while True:
        try:
            sq = int(input(f"{cur_turn} (1-9)")) #Player turn       
        except:
            print("Input should be between 0-9")
        if not isEmpty(sq-1):
            if cur_turn=="Player1":
                squares[sq-1]=1
            else:
                squares[sq-1]=2
            isOver()
           #### Cahange turn
            if cur_turn=="Player1":
               cur_turn="Player2"
            else:
               cur_turn="Player1"
            clear_screen()
        else:
            print("This square is occupied...")
        
        tictac()
        

def main():
    clear_screen()
    tictac()
    turn()
if __name__ == "__main__":
    main()