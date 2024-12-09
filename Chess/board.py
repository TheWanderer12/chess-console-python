from pieces import *


class Board:
    def __init__(self):
        self.extrawhitequeen = Queen("White", self, None)
        self.extrawhiterook = Rook("White", self, None)
        self.extrawhitebishop = Bishop("White", self, None)
        self.extrawhiteknight = Knight("White", self, None)

        self.mypieces = {}
        self.whiterook1 = Rook("White", self, ("A", 1))
        self.whiterook2 = Rook("White", self, ("H", 1))
        self.whiteknight1 = Knight("White", self, ("B", 1))
        self.whiteknight2 = Knight("White", self, ("G", 1))
        self.whitebishop1 = Bishop("White", self, ("C", 1))
        self.whitebishop2 = Bishop("White", self, ("F", 1))
        self.whitequeen = Queen("White", self, ("D", 1))
        self.whiteking = King("White", self, ("E", 1))
        self.whitepawn1 = Pawn("White", self, ("A", 2))
        self.whitepawn2 = Pawn("White", self, ("B", 2))
        self.whitepawn3 = Pawn("White", self, ("C", 2))
        self.whitepawn4 = Pawn("White", self, ("D", 2))
        self.whitepawn5 = Pawn("White", self, ("E", 2))
        self.whitepawn6 = Pawn("White", self, ("F", 2))
        self.whitepawn7 = Pawn("White", self, ("G", 2))
        self.whitepawn8 = Pawn("White", self, ("H", 2))

        self.extrablackqueen = Queen("Black", self, None)
        self.extrablackrook = Rook("Black", self, None)
        self.extrablackbishop = Bishop("Black", self, None)
        self.extrablackknight = Knight("Black", self, None)

        self.blackrook1 = Rook("Black", self, ("A", 8))
        self.blackrook2 = Rook("Black", self, ("H", 8))
        self.blackknight1 = Knight("Black", self, ("B", 8))
        self.blackknight2 = Knight("Black", self, ("G", 8))
        self.blackbishop1 = Bishop("Black", self, ("C", 8))
        self.blackbishop2 = Bishop("Black", self, ("F", 8))
        self.blackqueen = Queen("Black", self, ("D", 8))
        self.blackking = King("Black", self, ("E", 8))
        self.blackpawn1 = Pawn("Black", self, ("A", 7))
        self.blackpawn2 = Pawn("Black", self, ("B", 7))
        self.blackpawn3 = Pawn("Black", self, ("C", 7))
        self.blackpawn4 = Pawn("Black", self, ("D", 7))
        self.blackpawn5 = Pawn("Black", self, ("E", 7))
        self.blackpawn6 = Pawn("Black", self, ("F", 7))
        self.blackpawn7 = Pawn("Black", self, ("G", 7))
        self.blackpawn8 = Pawn("Black", self, ("H", 7))

        self.placePieces()

    def placePieces(self):
        self.mypieces = {("A", 8): self.blackrook1, ("B", 8): self.blackknight1,
                         ("C", 8): self.blackbishop1,
                         ("D", 8): self.blackqueen, ("E", 8): self.blackking,
                         ("F", 8): self.blackbishop2, ("G", 8): self.blackknight2,
                         ("H", 8): self.blackrook2, ("A", 7): self.blackpawn1, ("B", 7): self.blackpawn2,
                         ("C", 7): self.blackpawn3, ("D", 7): self.blackpawn4, ("E", 7): self.blackpawn5,
                         ("F", 7): self.blackpawn6, ("G", 7): self.blackpawn7,
                         ("H", 7): self.blackpawn8}

        for j in range(6, 2, -1):
            for i in range(ord("A"), ord("I")):
                self.mypieces[(chr(i), j)] = None

        self.mypieces.update({("A", 2): self.whitepawn1,
                              ("B", 2): self.whitepawn2,
                              ("C", 2): self.whitepawn3, ("D", 2): self.whitepawn4, ("E", 2): self.whitepawn5,
                              ("F", 2): self.whitepawn6,
                              ("G", 2): self.whitepawn7, ("H", 2): self.whitepawn8, ("A", 1): self.whiterook1,
                              ("B", 1): self.whiteknight1, ("C", 1): self.whitebishop1,
                              ("D", 1): self.whitequeen, ("E", 1): self.whiteking,
                              ("F", 1): self.whitebishop2, ("G", 1): self.whiteknight2, ("H", 1): self.whiterook2})

    def setPiece(self, position, piece):
        self.mypieces[piece.position] = None
        self.mypieces[position] = piece
        piece.position = position

    def getPiece(self, position):
        return self.mypieces.get(position)

    def makeMove(self, startPosition, endPosition, player):
        if self.getPiece(startPosition) is not None:
            if player == self.getPiece(startPosition).color:
                return self.getPiece(startPosition).move(endPosition)

    def displayBoard(self):
        myboard = [["(8)"],
                   ["(7)"],
                   ["(6)"],
                   ["(5)"],
                   ["(4)"],
                   ["(3)"],
                   ["(2)"],
                   ["(1)"],
                   ["   ", ["A "], ["B "], ["C "], ["D"], ["E "], ["F "], [" G"], ["H"]],
                   ]
        myvalues = []
        for i in self.mypieces.values():
            myvalues.append(i)
        i = 0
        j = 8
        m = 0
        while j <= 64 and m < 8:
            for k in range(i, j):
                if myvalues[k] is None:
                    myboard[m].append(["  "])
                else:
                    myboard[m].append([myvalues[k].getIcon()])
            i = j
            j += 8
            m += 1

        for i in range(9):
            print(myboard[i])
