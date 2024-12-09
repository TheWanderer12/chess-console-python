blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘",
              "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞",
              "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:
    def __init__(self, color, board, position):
        self._color = color
        self.__board = board
        self._position = position

    def getboard(self):
        return self.__board

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, mytuple):
        try:
            if (len(mytuple) != 2) or (len(str(mytuple[0])) != 1) or (len(str(mytuple[1])) != 1) or not \
                    (ord("A") <= ord(mytuple[0]) <= ord("H")) or not (0 < mytuple[1] < 9):
                print("invalid position!")
            else:
                self._position = mytuple
        except:
            print("Error in position")

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False

    def getName(self):
        return "Piece"

    def getIcon(self):
        if self.color == "White":
            return whiteIcons[self.getName()]
        else:
            return blackIcons[self.getName()]


class Knight(Piece):
    def getName(self):
        return "Knight"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        firstTest = False
        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                ((posdic[mypos[0]] - 2 == posdic[dest[0]] or
                  posdic[mypos[0]] + 2 == posdic[dest[0]]) and
                 (mypos[1] - 1 == dest[1] or mypos[1] + 1 == dest[1]) or
                 (posdic[mypos[0]] - 1 == posdic[dest[0]] or
                  posdic[mypos[0]] + 1 == posdic[dest[0]]) and
                 (mypos[1] - 2 == dest[1] or mypos[1] + 2 == dest[1])) and not (dest == mypos):
            firstTest = True

        if firstTest:
            if self.getboard().getPiece(dest) is None:
                return True

            if self.color == "White" and self.getboard().getPiece(dest).color == "White":
                return False
            elif self.color == "Black" and self.getboard().getPiece(dest).color == "Black":
                return False
            elif self.color == "White" and self.getboard().getPiece(dest).color == "Black":
                return True
            elif self.color == "Black" and self.getboard().getPiece(dest).color == "White":
                return True
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False


class Rook(Piece):
    def getName(self):
        return "Rook"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        reverseposdic = {value: key for (key, value) in posdic.items()}
        firstTest = False
        rightTest = False
        leftTest = False
        upTest = False
        downTest = False

        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                (dest[0] == mypos[0] or dest[1] == mypos[1]) and not (dest == mypos):
            firstTest = True

        if firstTest:
            if posdic[mypos[0]] < posdic[dest[0]]:
                rightcount = 0
                for i in range(posdic[mypos[0]] + 1, posdic[dest[0]]):
                    if self.getboard().getPiece((reverseposdic[i], mypos[1])) is None:
                        rightcount += 1
                if rightcount == posdic[dest[0]] - posdic[mypos[0]] - 1:
                    rightTest = True

            if posdic[mypos[0]] > posdic[dest[0]]:
                leftcount = 0
                for i in range(posdic[dest[0]] + 1, posdic[mypos[0]]):
                    if self.getboard().getPiece((reverseposdic[i], mypos[1])) is None:
                        leftcount += 1
                if leftcount == posdic[mypos[0]] - posdic[dest[0]] - 1:
                    leftTest = True

            if mypos[1] > dest[1]:
                downcount = 0
                for i in range(dest[1] + 1, mypos[1]):
                    if self.getboard().getPiece((mypos[0], i)) is None:
                        downcount += 1
                if downcount == mypos[1] - dest[1] - 1:
                    downTest = True

            if mypos[1] < dest[1]:
                upcount = 0
                for i in range(mypos[1] + 1, dest[1]):
                    if self.getboard().getPiece((mypos[0], i)) is None:
                        upcount += 1
                if upcount == dest[1] - mypos[1] - 1:
                    upTest = True

            if rightTest or leftTest or upTest or downTest:
                if self.getboard().getPiece(dest) is None or self.getboard().getPiece(dest).color != self.color:
                    return True
                else:
                    return False
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False


class Bishop(Piece):
    def getName(self):
        return "Bishop"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        reverseposdic = {value: key for (key, value) in posdic.items()}
        firstTest = False
        rightupTest = False
        rightdownTest = False
        leftupTest = False
        leftdownTest = False

        for i in range(1, 8):
            if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                    (posdic[dest[0]] == posdic[mypos[0]] - i and dest[1] == mypos[1] - i or
                     posdic[dest[0]] == posdic[mypos[0]] + i and dest[1] == mypos[1] + i or
                     posdic[dest[0]] == posdic[mypos[0]] - i and dest[1] == mypos[1] + i or
                     posdic[dest[0]] == posdic[mypos[0]] + i and dest[1] == mypos[1] - i) and not (dest == mypos):
                firstTest = True

        if firstTest:
            if posdic[mypos[0]] < posdic[dest[0]] and mypos[1] < dest[1]:
                rightupcount = 0
                distance = dest[1] - mypos[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] + i], mypos[1] + i)) is None:
                        rightupcount += 1
                if rightupcount == distance - 1:
                    rightupTest = True

            if posdic[mypos[0]] < posdic[dest[0]] and mypos[1] > dest[1]:
                rightdowncount = 0
                distance = mypos[1] - dest[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] + i], mypos[1] - i)) is None:
                        rightdowncount += 1
                if rightdowncount == distance - 1:
                    rightdownTest = True

            if posdic[mypos[0]] > posdic[dest[0]] and mypos[1] < dest[1]:
                leftupcount = 0
                distance = dest[1] - mypos[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] - i], mypos[1] + i)) is None:
                        leftupcount += 1
                if leftupcount == distance - 1:
                    leftupTest = True

            if posdic[mypos[0]] > posdic[dest[0]] and mypos[1] > dest[1]:
                leftdowncount = 0
                distance = mypos[1] - dest[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] - i], mypos[1] - i)) is None:
                        leftdowncount += 1
                if leftdowncount == distance - 1:
                    leftdownTest = True

            if rightupTest or leftupTest or rightdownTest or leftdownTest:
                if self.getboard().getPiece(dest) is None or self.getboard().getPiece(dest).color != self.color:
                    return True
                else:
                    return False
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False


class Queen(Piece):
    def getName(self):
        return "Queen"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        reverseposdic = {value: key for (key, value) in posdic.items()}

        rightTest = False
        leftTest = False
        upTest = False
        downTest = False
        rightupTest = False
        rightdownTest = False
        leftupTest = False
        leftdownTest = False

        rookTest = False
        bishopTest = False

        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                (dest[0] == mypos[0] or dest[1] == mypos[1]) and not (dest == mypos):
            rookTest = True

        for i in range(1, 8):
            if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                    (posdic[dest[0]] == posdic[mypos[0]] - i and dest[1] == mypos[1] - i or
                     posdic[dest[0]] == posdic[mypos[0]] + i and dest[1] == mypos[1] + i or
                     posdic[dest[0]] == posdic[mypos[0]] - i and dest[1] == mypos[1] + i or
                     posdic[dest[0]] == posdic[mypos[0]] + i and dest[1] == mypos[1] - i) and not (dest == mypos):
                bishopTest = True

        if bishopTest:  # here basically rook and bishop tests combined
            if posdic[mypos[0]] < posdic[dest[0]] and mypos[1] < dest[1]:
                rightupcount = 0
                distance = dest[1] - mypos[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] + i], mypos[1] + i)) is None:
                        rightupcount += 1
                if rightupcount == distance - 1:
                    rightupTest = True

            if posdic[mypos[0]] < posdic[dest[0]] and mypos[1] > dest[1]:
                rightdowncount = 0
                distance = mypos[1] - dest[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] + i], mypos[1] - i)) is None:
                        rightdowncount += 1
                if rightdowncount == distance - 1:
                    rightdownTest = True

            if posdic[mypos[0]] > posdic[dest[0]] and mypos[1] < dest[1]:
                leftupcount = 0
                distance = dest[1] - mypos[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] - i], mypos[1] + i)) is None:
                        leftupcount += 1
                if leftupcount == distance - 1:
                    leftupTest = True

            if posdic[mypos[0]] > posdic[dest[0]] and mypos[1] > dest[1]:
                leftdowncount = 0
                distance = mypos[1] - dest[1]
                for i in range(1, distance):
                    if self.getboard().getPiece((reverseposdic[posdic[mypos[0]] - i], mypos[1] - i)) is None:
                        leftdowncount += 1
                if leftdowncount == distance - 1:
                    leftdownTest = True

            if rightupTest or rightdownTest or leftupTest or leftdownTest:
                if self.getboard().getPiece(dest) is None or self.getboard().getPiece(dest).color != self.color:
                    return True
                else:
                    return False

        if rookTest:
            if posdic[mypos[0]] < posdic[dest[0]]:
                rightcount = 0
                for i in range(posdic[mypos[0]] + 1, posdic[dest[0]]):
                    if self.getboard().getPiece((reverseposdic[i], mypos[1])) is None:
                        rightcount += 1
                if rightcount == posdic[dest[0]] - posdic[mypos[0]] - 1:
                    rightTest = True

            if posdic[mypos[0]] > posdic[dest[0]]:
                leftcount = 0
                for i in range(posdic[dest[0]] + 1, posdic[mypos[0]]):
                    if self.getboard().getPiece((reverseposdic[i], mypos[1])) is None:
                        leftcount += 1
                if leftcount == posdic[mypos[0]] - posdic[dest[0]] - 1:
                    leftTest = True

            if mypos[1] > dest[1]:
                downcount = 0
                for i in range(dest[1] + 1, mypos[1]):
                    if self.getboard().getPiece((mypos[0], i)) is None:
                        downcount += 1
                if downcount == mypos[1] - dest[1] - 1:
                    downTest = True

            if mypos[1] < dest[1]:
                upcount = 0
                for i in range(mypos[1] + 1, dest[1]):
                    if self.getboard().getPiece((mypos[0], i)) is None:
                        upcount += 1
                if upcount == dest[1] - mypos[1] - 1:
                    upTest = True

            if rightTest or leftTest or upTest or downTest:
                if self.getboard().getPiece(dest) is None or self.getboard().getPiece(dest).color != self.color:
                    return True
                else:
                    return False
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False


class King(Piece):
    def getName(self):
        return "King"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        firstTest = False

        rookTest = False
        bishopTest = False

        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                (posdic[dest[0]] == posdic[mypos[0]] and (dest[1] == mypos[1] - 1 or
                                                          dest[1] == mypos[1] + 1) or (
                    posdic[dest[0]] == posdic[mypos[0]] - 1 or
                    posdic[dest[0]] == posdic[mypos[0]] + 1) and dest[1] == mypos[1]) and not (dest == mypos):
            rookTest = True

        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and \
                (posdic[dest[0]] == posdic[mypos[0]] - 1 and dest[1] == mypos[1] - 1 or
                 posdic[dest[0]] == posdic[mypos[0]] + 1 and dest[1] == mypos[1] + 1 or
                 posdic[dest[0]] == posdic[mypos[0]] - 1 and dest[1] == mypos[1] + 1 or
                 posdic[dest[0]] == posdic[mypos[0]] + 1 and dest[1] == mypos[1] - 1) and not (
                posdic[dest[0]] == posdic[mypos[0]] and dest[1] == mypos[1]):
            bishopTest = True

        if rookTest or bishopTest:
            firstTest = True

        if firstTest:
            if self.getboard().getPiece(dest) is None or self.getboard().getPiece(dest).color != self.color:
                return True
            else:
                return False
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False


class Pawn(Piece):
    def getName(self):
        return "Pawn"

    def checkMove(self, dest):
        mypos = self.position
        posdic = {"A": 1, "B": 2, "C": 3, "D": 4,
                  "E": 5, "F": 6, "G": 7, "H": 8}
        whiteTest = False
        blackTest = False
        whitenormTest = False
        blacknormTest = False

        if 0 < posdic[dest[0]] < 9 and 0 < dest[1] < 9 and not (dest == mypos):
            if mypos[1] == 2 and dest[1] == 4 and self.color == "White":
                whiteTest = True
            elif mypos[1] == 7 and dest[1] == 5 and self.color == "Black":
                blackTest = True
            elif dest[1] == mypos[1] + 1 and self.color == "White":
                whitenormTest = True
            elif dest[1] == mypos[1] - 1 and self.color == "Black":
                blacknormTest = True

        killTest = False
        if self.color == "White" and dest[1] == mypos[1] + 1 and (
                posdic[dest[0]] == posdic[mypos[0]] + 1 or posdic[dest[0]] == posdic[mypos[0]] - 1):
            killTest = True
        if self.color == "Black" and dest[1] == mypos[1] - 1 and (
                posdic[dest[0]] == posdic[mypos[0]] + 1 or posdic[dest[0]] == posdic[mypos[0]] - 1):
            killTest = True

        if whiteTest or whitenormTest:
            nonecount = 0
            distance = dest[1] - mypos[1]
            for i in range(1, distance + 1):
                if self.getboard().getPiece((mypos[0], mypos[1] + i)) is None:
                    nonecount += 1
            if nonecount == distance:
                return True

        if blackTest or blacknormTest:
            blacknonecount = 0
            distance = mypos[1] - dest[1]
            for i in range(1, distance + 1):
                if self.getboard().getPiece((mypos[0], mypos[1] - i)) is None:
                    blacknonecount += 1
            if blacknonecount == distance:
                return True

        if killTest:
            if self.getboard().getPiece(dest) is not None and self.getboard().getPiece(dest).color != self.color:
                return True
            else:
                return False
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.getboard().setPiece(dest, self)
            return True
        return False
