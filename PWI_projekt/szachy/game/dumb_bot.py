import random
import pygame as pg
from pygame import mixer
import numpy as np
from PWI_projekt.szachy.game.pieces.pawn import *
from PWI_projekt.szachy.game.pieces.rook import *
from PWI_projekt.szachy.game.pieces.king import *
from PWI_projekt.szachy.game.pieces.queen import *
from PWI_projekt.szachy.game.pieces.bishop import *
from PWI_projekt.szachy.game.pieces.knight import *
from PWI_projekt.szachy.game.base_piece import *
from PWI_projekt.szachy.game.game import *
import random

class DumbBot:
    def __init__(self, color, board):
        self.color = color

        self.w_attacked = board.w_attacked  # Initialize w_attacked
        self.b_attacked = board.b_attacked  # Initialize b_attacked

    def get_random_move(self, board):
        valid_moves = self.get_all_valid_moves(board)
        if not valid_moves:
            return None

        return random.choice(valid_moves)

    def get_all_valid_moves(self, board):
        valid_moves = []

        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                #print("piece", piece)
                if piece != 0 and piece.color == self.color:
                    if isinstance(piece, King):
                        possible_moves_db = piece.possible_moves_f(board, self.w_attacked, self.b_attacked)
                        cośtam = piece.possible_moves

                    else:
                        possible_moves_db = piece.possible_moves_f(board)
                        cośtam = piece.possible_moves


                    #print("possible moves",possible_moves_db)
                    print("cośtam", cośtam)

                    # Check if possible_moves is None
                    if cośtam is not None and cośtam is not []:
                        for move in cośtam:
                            valid_moves.append(((i, j), move))
        print("valid moves:", valid_moves)
        return valid_moves
