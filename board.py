from pieces import *


class Board:
    def __init__(self, pos=None):
        self.board = [[None for j in range(8)] for i in range(8)]
        self.set_pieces()


    def set_pieces(self):
<<<<<<< HEAD
        # for j in range(8):
        #     self.board[1][j] = Pawn(color='white')
        #     self.board[6][j] = Pawn(color='black')
        # for j, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
        #     self.board[0][j] = piece(color='white')
        #     self.board[7][j] = piece(color='black')
        self.board[2][3] = Pawn(color='white')
        self.board[3][4] = Pawn(color='black')


    def make_move_from_uci(self, move: 'uci_format'):

        self.show()

        from_file, from_rank, to_file, to_rank = move
        from_file, to_file = ord(from_file) - ord('a'), ord(to_file) - ord('a')
        from_rank, to_rank = int(from_rank) - 1, int(to_rank) - 1

        print(from_file, from_rank, to_file, to_rank)

        piece = self.board[from_rank][from_file]
        self.board[to_rank][to_file] = piece
        self.board[from_rank][from_file] = None

        self.show()



    def show(self):
        print('\n'*3)
        for i in range(7, -1, -1):
=======
        for j in range(8):
            self.board[1][j] = Pawn(color='white')
            self.board[6][j] = Pawn(color='black')
        for j, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
            self.board[0][j] = piece(color='white')
            self.board[7][j] = piece(color='black')

    def show(self):
        print('\n'*3)
        for i in range(8):
>>>>>>> 1f8a3b105b9d76b1ade139400c0e3f78606ac2e5
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    print(piece, end='  ')
                else:
                    print('. ', end='  ')
            print('\n')
        print('\n'*3)
        