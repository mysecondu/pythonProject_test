import numpy as np
import random
from game.base_piece import Piece

class DumbBot:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        pieces = board.get_pieces_by_color(self.color)
        piece = random.choice(pieces)

        if piece.possible_moves:
            move = random.choice(piece.possible_moves)
            board.move_piece(piece.pos, move)
        elif piece.possible_attacks:
            attack = random.choice(piece.possible_attacks)
            board.move_piece(piece.pos, attack)
