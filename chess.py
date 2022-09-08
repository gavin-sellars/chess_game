from asyncio.windows_events import NULL
from board import Board

class Chess():

    def __init__(self):
        # replace `pass` with the desired attributes and add any 
        # additional parameters to the function

        pass

    def promotion(self):
        # add any parameters necessary and replace the body with
        # functionality on promoting a Pawn that has reached the 
        # end of the board
        pass

    def move(self, initial, final):

        changingBoard = Board.accessBoard()

        if len(initial) != 2 or len(final) != 2:
            print("\nYour moves must be in the format of LETTER + NUMBER (i.e. e2 or g6)")

            return

        if changingBoard[7-int(initial[1])][int(initial[0])] == NULL:
            print("\nYou have attempted to make an invalid move. Please try again.")

            return

        
        changingBoard[7-int(final[1])][int(final[0])] = changingBoard[7-int(initial[1])][int(initial[0])]
        changingBoard[7-int(initial[1])][int(initial[0])] = NULL

        global finalBoard
        finalBoard = "\n"

        for i in range(8):
            for j in range(8):
                if changingBoard[i][j] == 0:
                    finalBoard = finalBoard + "| "
                else:
                    finalBoard = finalBoard + "|" + str(changingBoard[i][j])
            finalBoard = finalBoard + "|\n"

        print(finalBoard)

        return changingBoard
        
    

        # add any parameters necessary and replace the body with
        # functionality of moving a a piece from its current location
        # to a destination
        pass
    
def translate(move):

    global restart
    restart = 0

    if move[0].isalpha() == False or move[1].isalpha() == True:
        return("restart")
            

    backendMove = ""
    
    letters = "abcdefgh"

    for i in range(2):

        if move[i].isalpha():
            move = move.lower()

        for j in range(8):
            if move[i] == letters[j]:
                backendMove = backendMove + str(j)
            elif move[i] == str(j+1):
                backendMove = backendMove + str(j)
                
    return backendMove
    




if __name__ == "__main__":
    chess = Chess()

    while True:
        start = input("From: ")
        to = input("To: ")
        
        # translate is a helper method to turn the user input into
        # a representation depending on how the board is represented
        start = translate(start)
        to = translate(to)

        if start == "restart" and to == "restart":
            print("\nYour moves must be in the format of LETTER + NUMBER (i.e. e2 or g6)\n")
            continue

        if start == None or to == None:
            continue

        chess.move(start, to)

        # check for promotion pawns

        '''
        i = 0
        while i < 8:
            if not chess.turn and chess.board.board[0][i] != None and \
                chess.board.board[0][i].name == 'P':
                chess.promotion((0, i))
                break
            elif chess.turn and chess.board.board[7][i] != None and \
                chess.board.board[7][i].name == 'P':
                chess.promotion((7, i))
                break
            i += 1
        '''

        #print(finalBoard)