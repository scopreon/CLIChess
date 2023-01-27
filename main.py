from pieces import *
from board import *
from game import *


def dialog():
    print("Welcome to CLIChess!\n"
          "1 - Start new game\n"
          "2 - Load game\n"
          "3 - Settings\n"
          "4 - Exit")

if __name__ == '__main__':
    dialog()
    game1 = Game()
    game1.start()

    print("By SAUL COOPERMAN")
    print("Made in 2015")
    # print((board.board[6][4]).possibleMoves(board.board))
