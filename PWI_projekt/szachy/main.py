import pygame as pg
import numpy as np
from game.board import *
from game.game import *
from game.options import *
from time import *
from game.dumb_bot import *


pg.init()

def main():
    menu = Menu()
    selected_option = menu.run()

    screen_size = 800
    screen = pg.display.set_mode((screen_size, screen_size))
    pg.display.set_caption("Szachy")
    white = (220, 230, 255)
    brown = (205, 133, 63)
    board = ChessBoard(screen_size, (white, brown), screen)

    if selected_option == "Player vs Player":



        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break

            screen.fill((0, 0, 0))
            board.draw_board()
            highlight(screen)
            board.move_piece()
            board.draw_pieces()

            pg.display.flip()



    elif selected_option == "Bot vs Bot":
        print(selected_option)





    elif "Player vs Bot" in selected_option:
        i = 0
        # Initialize DumbBot
        dumb_bot = DumbBot("b", board)
        while True:
            i += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break

            screen.fill((0, 0, 0))
            board.draw_board()
            highlight(screen)

            if board.turn == "b":
                bot_move = dumb_bot.get_random_move(board.board)
                print("bot move",bot_move)

                if bot_move != None:
                    start_pos, end_pos = bot_move
                    piece = board.board[start_pos[0]][start_pos[1]]
                    piece.move_to(board.board, end_pos[0], end_pos[1])
                    board.turn = "w"
                    print(board.turn)


                print("bot", i)



            # Player's turn
            else:
                board.move_piece()
                board.draw_pieces()

            pg.display.flip()










    """elif (selected_option == "Bot vs Bot" or selected_option == "Player vs Bot - White - Dumb Bot"      #Nie działa dla tych opcji
        or selected_option == "Player vs Bot - White - Smart Bot"
        or selected_option == "Player vs Bot - Black - Dumb Bot"
        or selected_option == "Player vs Bot - White - Dumb Bot"):

        print(selected_option)"""

if __name__ == "__main__":
    main()
