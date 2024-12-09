from board import Board

from pieces import *


class Chess:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        if self.currentPlayer == "White":
            self.currentPlayer = "Black"
        else:
            self.currentPlayer = "White"

    def isStringValidMove(self, moveStr):
        try:
            if len(moveStr) == 5 and ord("A") <= ord(moveStr[0]) <= ord("H") and ord("A") <= ord(moveStr[3]) <= ord("H")\
                    and 0 < int(moveStr[1]) < 9 and 0 < int(moveStr[4]) < 9 and moveStr[2] == " ":
                return True
            else:
                return False
        except:
            return False

    def play(self):
        while True:
            exitloop = False
            self.board.displayBoard()
            print(f"{self.currentPlayer}'s turn. Enter a move: ")
            move = input()
            if move == "EXIT":
                break

            while not self.isStringValidMove(move):
                print(f"{self.currentPlayer}'s turn. Enter a move: ")
                move = input()
                if move == "EXIT":
                    exitloop = True
            if exitloop:
                break

            movesplit = move.split(" ")
            posanddest = ((movesplit[0][0], int(movesplit[0][1])), (movesplit[1][0], int(movesplit[1][1])))
            while not self.board.makeMove(posanddest[0], posanddest[1], self.currentPlayer):
                print(f"{self.currentPlayer}'s turn. Enter a move: ")
                move = input()
                if move == "EXIT":
                    exitloop = True
                    break

                while not self.isStringValidMove(move):
                    print(f"{self.currentPlayer}'s turn. Enter a move: ")
                    move = input()
                    if move == "EXIT":
                        exitloop = True
                        break
                movesplit = move.split(" ")
                posanddest = ((movesplit[0][0], int(movesplit[0][1])), (movesplit[1][0], int(movesplit[1][1])))

            if exitloop:
                break

            choices = ["Queen", "Rook", "Bishop", "Knight"]
            for i in range(ord("A"), ord("I")):
                if self.currentPlayer == "White" and self.board.getPiece((chr(i), 8)) is not None \
                        and self.board.getPiece((chr(i), 8)).getName() == "Pawn":
                    choice = input("Which piece would you like to promote to? Queen, Rook, Bishop or Knight. ")
                    while choice not in choices:
                        choice = input("Which piece would you like to promote to? Queen, Rook, Bishop or Knight. ")
                    if choice == "Queen":
                        self.board.setPiece(posanddest[1], self.board.extrawhitequeen)
                    elif choice == "Rook":
                        self.board.setPiece(posanddest[1], self.board.extrawhiterook)
                    elif choice == "Bishop":
                        self.board.setPiece(posanddest[1], self.board.extrawhitebishop)
                    elif choice == "Knight":
                        self.board.setPiece(posanddest[1], self.board.extrawhiteknight)
                elif self.currentPlayer == "Black" and self.board.getPiece((chr(i), 1)) is not None \
                        and self.board.getPiece((chr(i), 1)).getName() == "Pawn":
                    choice = input("Which piece would you like to promote to? Queen, Rook, Bishop or Knight.")
                    while choice not in choices:
                        choice = input("Which piece would you like to promote to? Queen, Rook, Bishop or Knight.")
                    if choice == "Queen":
                        self.board.setPiece(posanddest[1], self.board.extrablackqueen)
                    elif choice == "Rook":
                        self.board.setPiece(posanddest[1], self.board.extrablackrook)
                    elif choice == "Bishop":
                        self.board.setPiece(posanddest[1], self.board.extrablackbishop)
                    elif choice == "Knight":
                        self.board.setPiece(posanddest[1], self.board.extrablackknight)
            self.swapPlayers()


if __name__ == "__main__":
    game = Chess()
    game.play()
