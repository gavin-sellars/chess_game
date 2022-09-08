from asyncio.windows_events import NULL
from typing import final
from piece import Bishop, King, Knight, Pawn, Queen, Rook


class Board():

    global boardLayout

    boardLayout =   [[Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)], 
                    [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)], 
                    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                    [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
                    [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)]]        

    def accessBoard():
        sendToChessBoard = boardLayout
        return sendToChessBoard

    def print_board(self):

        finalBoard = "\n"

        for i in range(8):
            for j in range(8):
                if boardLayout[i][j] == 0:
                    finalBoard = finalBoard + "| "
                else:
                    finalBoard = finalBoard + "|" + str(boardLayout[i][j])
            finalBoard = finalBoard + "|\n"

        print(finalBoard)

Board().print_board()