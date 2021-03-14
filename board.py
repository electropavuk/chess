from pieces import *


class Board:
    def __init__(self, pos=None):
        self.board = [[None for j in range(8)] for i in range(8)]
        self.set_pieces()


    def set_pieces(self):
        for j in range(8):
            self.board[1][j] = Pawn(color='white')
            self.board[6][j] = Pawn(color='black')
        for j, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
            self.board[0][j] = piece(color='white')
            self.board[7][j] = piece(color='black')

    def show(self):
        print('\n'*3)
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    print(piece, end='  ')
                else:
                    print('. ', end='  ')
            print('\n')
        print('\n'*3)
        