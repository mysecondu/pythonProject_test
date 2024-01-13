import numpy as np
import random
from game.base_piece import *

class DumbBot:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        pieces = [piece for row in board for piece in row if isinstance(piece, Piece) and piece.color == self.color]
        random_piece = random.choice(pieces)

        random_move = random.choice(random_piece.possible_moves)

        return random_piece.pos, random_move
