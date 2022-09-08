class Piece():

    def __init__(self, color):
        self.color = color
        # add any additional parameters
        # standard initiation of a piece 
        pass
        
    def is_valid_move(self):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        # replace the body and return a string with how you want your piece
        # to be printed as when `print([A Piece Object])` is called
        return ''
        
# I'll add which parameters I generally used for the specific subclasses
# in the following Rook class, but note you may need more or less depending
# on your specific implementation
class Rook(Piece):
    def __init__(self, color):
        # super().__init__(...) can be super helpful in just calling the 
        # parent init function to avoid the same lines of code
        self.color = color

    def __str__(self):
        if super().is_white():
            return "R"

        else:
            return '\033[92m' + 'R' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if super().is_white():
            return "K"

        else:
            return '\033[92m' + 'K' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass

class Bishop(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if super().is_white():
            return "B"

        else:
            return '\033[92m' + 'B' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass

class Queen(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if super().is_white():
            return "Q"

        else:
            return '\033[92m' + 'Q' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass

class King(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if super().is_white():
            return "K"

        else:
            return '\033[92m' + 'K' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass
    
    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def is_valid_move(self, board, start, to):
        return False

class Pawn(Piece):
    def __init__(self, color):
        self.color = color
        pass

    def __str__(self):
        if super().is_white():
            return "P"

        else:
            return '\033[92m' + 'P' + '\033[0m'

    def is_valid_move(self, board, start, to):
        pass