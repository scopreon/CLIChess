from pieces import *
class Format:
    end = '\033[0m'
    underline = '\033[4m'


pieces = [{
    "Pawn": "♟",
    "Rook": "♜",
    "King": "♚",
    "Queen": "♛",
    "Bishop": "♝",
    "Knight": "♞"
},
    {
    "Pawn": "♙",
    "Rook": "♖",
    "King": "♔",
    "Queen": "♕",
    "Bishop": "♗",
    "Knight": "♘"
    }]

class Board:
    board = []
    printed=False
    def isInCheck(self,color):
        pass
    def oppMoves(self,color):
        notMoves = []
        for x in range(0, 8):
            for y in range(0, 8):
                if self.board[x][y] is not None and self.board[x][y].color != color and self.board[x][y].name != "King":
                    notMoves += self.board[x][y].possibleMoves(self, True)
        return notMoves
    def isCheckmate(self, color):
        notMoves=self.oppMoves(color)

        # self.printBoard(notMoves)
        for x in range(0,8):
            for y in range(0,8):
                if self.board[x][y] is not None and self.board[x][y].name == "King" and \
                        len(self.board[x][y].possibleMoves(self,False))==0 and [x,y] in notMoves and self.board[x][y].color==color:
                    return True
# [x,y] not in notMoves
        # can you take the piece you just moved?
        # can you block the piece
        # clear up code a bit
        return False

    def printBoard(self,greyOut):
        if self.printed:
            print("\033[F" * 11)
        format=Format()
        print(format.underline,end="")
        for x in range(0,8):
            print(format.end+str(8-x)+"|"+format.underline, end="")
            for y in range(0,8):
                # self.board[x][y].name

                if [x,y] in greyOut:
                    print("█",end="|")
                elif self.board[x][y] is not None:
                    # print(self.board[x][y].color)
                    print(pieces[self.board[x][y].color][self.board[x][y].name],end="|")
                else:
                    print(" ",end="|")
            print()
        print(format.end,end="")
        print(" |"+"|".join(list("ABCDEFGH"))+"|")
        if self.printed:
            print("  \r",end="")
        # self.printed = True

    def __init__(self):
        self.board = [
            [Rook(1),   Knight(1),  Bishop(1),  Queen(1),   King(1),    Bishop(1),  Knight(1),  Rook(1)],
            [Pawn(1),   Pawn(1),    Pawn(1),    Pawn(1),    Pawn(1),    Pawn(1),    Pawn(1),    Pawn(1)],
            [None,      None,       None,       None,       None,       None,       None,       None],
            [None,      None,       None,       None,       None,       None,       None,       None],
            [None,      None,       None,       None,       None,       None,       None,       None],
            [None,      None,       None,       None,       None,       None,       None,       None],
            [Pawn(0),   Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0)],
            [Rook(0),   Knight(0),  Bishop(0),  Queen(0),   King(0),    Bishop(0),  Knight(0),  Rook(0)]
        ]
        # self.board = [
        #     [Rook(1),   Knight(1),  Bishop(1),  Queen(1),   King(1),    Bishop(1),  Knight(1),  Rook(1)],
        #     [Pawn(1),   Pawn(1),    Pawn(1),    Pawn(1),    Pawn(1),    None,    Pawn(1),    Pawn(1)],
        #     [None,      None,       None,       Queen(0),       None,       None,       None,       None],
        #     [None,      None,       None,       None,       None,       Rook(0),    None,       None],
        #     [None,      None,       None,       None,       None,       None,       None,       None],
        #     [None,      None,       None,       None,       None,       None,       None,       None],
        #     [Pawn(0),   Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0),    Pawn(0)],
        #     [Rook(0),   Knight(0),  Bishop(0),  Queen(0),   King(0),    Bishop(0),  Knight(0),  Rook(0)]
        # ]
        for x in range(0,8):
            for y in range(0,8):
                if self.board[x][y] is not None:
                    self.board[x][y].posX = x
                    self.board[x][y].posY = y

    def move(self,loc1,loc2):
        self.board[loc2[0]][loc2[1]] = self.board[loc1[0]][loc1[1]]
        (self.board[loc2[0]][loc2[1]]).posX = loc2[0]
        (self.board[loc2[0]][loc2[1]]).posY = loc2[1]
        self.board[loc1[0]][loc1[1]] = None


    # █