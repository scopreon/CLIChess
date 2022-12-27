class Piece():
    color = None
    posX = None
    posY = None
    name = None

    def __init__(self, color):
        self.color = color
        self.name = type(self).__name__


class Rook(Piece):
    def possibleMoves(self, board, takeSameColor):
        moves = []
        for dY in [-1, 0, 1]:
            for dX in [-1, 0, 1]:
                x = self.posX
                y = self.posY
                if abs(dY + dX) == 1 and abs(dY) + abs(dX) != 0:
                    while True:
                        y += dY
                        x += dX
                        if 8 > y > -1 and 8 > x > -1:
                            if board.board[x][y] is None or (board.board[x][y].color != self.color or takeSameColor):
                                moves.append([x, y])
                                if board.board[x][y] is not None: break
                            else:
                                break
                        else:
                            break

        return moves


class Bishop(Piece):
    def possibleMoves(self, board, takeSameColor):
        moves = []
        for dY in [-1, 0, 1]:
            for dX in [-1, 0, 1]:
                x = self.posX
                y = self.posY
                if abs(dY + dX) != 1 and abs(dY)+abs(dX) != 0:
                    while True:
                        y += dY
                        x += dX
                        if 8 > y > -1 and 8 > x > -1:
                            if board.board[x][y] is None or (board.board[x][y].color != self.color or takeSameColor):
                                moves.append([x, y])
                                if board.board[x][y] is not None: break
                            else:
                                break
                        else:
                            break

        return moves


class Knight(Piece):
    def possibleMoves(self, board,takeSameColor):
        moves = []
        for x in range(0,8):
            for y in range(0,8):
                if abs(self.posX-x) * abs(self.posY-y) == 2:
                    if board.board[x][y] is None or (board.board[x][y].color != self.color or takeSameColor):
                        moves.append([x,y])
                        if board.board[x][y] is not None: break
        return moves


class King(Piece):
    moved = False
    def inCheck(self,board):
        return True
    def possibleMoves(self, board,takeSameColor):
        notMoves = board.oppMoves(self.color)
        moves = []
        for dY in [-1, 0, 1]:
            for dX in [-1, 0, 1]:
                x = self.posX+dX
                y = self.posY+dY
                if 8 > y > -1 and 8 > x > -1 and abs(dY)+abs(dX) != 0:
                    if board.board[x][y] is None or (board.board[x][y].color != self.color or takeSameColor):
                        if [x, y] not in notMoves:
                            moves.append([x, y])
        # castling
        if not self.moved:
            if board.board[self.posX][self.posY+1] is None and board.board[self.posX][self.posY+2] is None and \
                    board.board[self.posX][self.posY+3].name=="Rook" and board.board[self.posX][self.posY+3].color == self.color:
                if [self.posX, self.posY + 2] not in notMoves and [self.posX, self.posY + 1] not in notMoves:
                    moves.append([self.posX,self.posY+2])
            if board.board[self.posX][self.posY-1] is None and board.board[self.posX][self.posY-2] is None and \
                    board.board[self.posX][self.posY-3] is None and board.board[self.posX][self.posY-4].name=="Rook" and \
                    board.board[self.posX][self.posY-4].color == self.color:
                if [self.posX, self.posY - 2] not in notMoves and [self.posX, self.posY - 1] not in notMoves:
                    moves.append([self.posX,self.posY-2])
        return moves


class Queen(Piece):
    def possibleMoves(self, board,takeSameColor):
        moves = []
        for dY in [-1, 0, 1]:
            for dX in [-1, 0, 1]:
                x = self.posX
                y = self.posY
                if abs(dY)+abs(dX) != 0:
                    while True:
                        y += dY
                        x += dX
                        if 8 > y > -1 and 8 > x > -1:
                            if board.board[x][y] is None or (board.board[x][y].color != self.color or takeSameColor):
                                moves.append([x, y])
                                if board.board[x][y] is not None: break
                            else:
                                break
                        else:
                            break

        return moves

class Pawn(Piece):
    def possibleMoves(self, board,takeSameColor):
        moves = []
        diff=-1+self.color*2
        if board.board[self.posX + diff][self.posY] is None:
            moves.append([self.posX + diff,self.posY])
            if board.board[self.posX + diff*2][self.posY] is None and ((self.posX==1 and self.color)or(self.posX==6 and not self.color)):
                moves.append([self.posX + diff*2, self.posY])
        if 8 > self.posY+1 > -1 and board.board[self.posX + diff][self.posY+1] is not None:
            if board.board[self.posX + diff][self.posY+1].color != self.color:
                moves.append([self.posX + diff, self.posY+1])
        if 8 > self.posY-1 > -1 and board.board[self.posX + diff][self.posY-1] is not None:
            if board.board[self.posX + diff][self.posY-1].color != self.color:
                moves.append([self.posX + diff, self.posY-1])

        return moves
