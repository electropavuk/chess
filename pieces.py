


class Piece:
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Pawn(Piece):
    def __init__(self, color):
        self.name = 'wP' if color == 'white' else 'bP'


class Knight(Piece):
    def __init__(self, color):
        self.name = 'wN' if color == 'white' else 'bN'


class Bishop(Piece):
    def __init__(self, color):
        self.name = 'wB' if color == 'white' else 'bB'


class Rook(Piece):
    def __init__(self, color):
        self.name = 'wR' if color == 'white' else 'bR'


class King(Piece):
    def __init__(self, color):
        self.name = 'wK' if color == 'white' else 'bK'


class Queen(Piece):
    def __init__(self, color):
        self.name = 'wQ' if color == 'white' else 'bQ'

