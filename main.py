from pieces import *
from board import *

def boardCoords(loc):
    loc[0] = ord(loc[0].upper())-65
    loc[1] = int(loc[1])-1
    # loc=list(map(int,loc))

    return [7-loc[1],loc[0]]

def getPiece():
    pass

def getLocation():
    pass

def dialog():
    pass

if __name__ == '__main__':
    board = Board()
    board.printBoard([])
    if board.isCheckmate(1):
        print("checkmate")
    # board.printBoard([])
    color = 0
    while True:
        while True:
            a = boardCoords(list(input()))
            if board.board[a[0]][a[1]] is None or board.board[a[0]][a[1]].color!=color:
                print("NOT VALID PIECE")
                continue
            movesAvailable=(board.board[a[0]][a[1]]).possibleMoves(board,False)
            board.printBoard(movesAvailable)
            b = input()
            if b == "p":
                board.printBoard([])
                continue
            b = boardCoords(list(b))
            while b not in movesAvailable:
                print("NOT VALID MOVE")
                b=input()
                if b=="p":
                    board.printBoard([])
                    break
                b = boardCoords(list(b))
            if b!="p":
                board.move(a, b)
                if board.board[b[0]][b[1]].name == "King":
                    if b[1]-a[1]==2:
                        board.move([a[0],7],[a[0],5])
                    if b[1]-a[1]==-2:
                        board.move([a[0],0],[a[0],2])
                    board.board[b[0]][b[1]].moved=True
                break
        color = abs(color-1)
        board.printBoard([])
        if board.isCheckmate(color):
            print("checkmate")
            break

    print("By SAUL COOPERMAN")
    print("Made in 2015")
    # print((board.board[6][4]).possibleMoves(board.board))
