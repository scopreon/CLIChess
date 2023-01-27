from board import *


def boardCoords(loc):
    loc[0] = ord(loc[0].upper())-65
    loc[1] = int(loc[1])-1
    # loc=list(map(int,loc))

    return [7-loc[1], loc[0]]


class Game():

    def getPiece(self, color):
        a = boardCoords(list(input()))
        while self.board.board[a[0]][a[1]] is None or self.board.board[a[0]][a[1]].color != color:
            print("NOT VALID PIECE")
            a = boardCoords(list(input()))
        return a

    def getLocation(self, movesAvailable):
        b = input()
        print("i1")
        if b == "p":
            self.board.printBoard([])
            return "p"
        b = boardCoords(list(b))
        while b not in movesAvailable:
            print("NOT VALID MOVE")
            b = input()
            if b == "p":
                self.board.printBoard([])
                return "p"
            b = boardCoords(list(b))
        print("exit")
        return b

    board = None

    def __init__(self):
        self.board = Board()

    def start(self):
        self.board.printBoard([])
        if self.board.isCheckmate(1):
            print("checkmate")
        # board.printBoard([])
        color = 0
        while True:
            while True:
                a = self.getPiece(color)
                movesAvailable = (self.board.board[a[0]][a[1]]).possibleMoves(self.board, False)
                self.board.printBoard(movesAvailable)
                b = self.getLocation(movesAvailable)

                if b == "p":
                    continue

                self.board.move(a, b)
                if self.board.board[b[0]][b[1]].name == "King":
                    if b[1] - a[1] == 2:
                        self.board.move([a[0], 7], [a[0], 5])
                    if b[1] - a[1] == -2:
                        self.board.move([a[0], 0], [a[0], 2])
                    self.board.board[b[0]][b[1]].moved = True
                break
            color = abs(color - 1)
            self.board.printBoard([])
            if self.board.isCheckmate(color):
                print("checkmate")
                break

    def printBoard(self):
        self.board.printBoard()