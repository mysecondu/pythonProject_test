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





    elif "Player vs Bot" in selected_option:   ##only for player white "w"
        i = 0

        the_dumb_bot = DumbBot("b", board)
        while True:
            i += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break




            if board.turn == "b":
                bot_move = the_dumb_bot.get_random_move(board.board)

                if bot_move != None:
                    screen.fill((0, 0, 0))
                    board.draw_board()

                    start_pos, end_pos = bot_move
                    print(start_pos)
                    print(end_pos)

                    board.move_piece_bot(start_pos, end_pos)
                    board.draw_pieces()




            # Player's turn
            else:
                screen.fill((0, 0, 0))
                board.draw_board()
                highlight(screen)
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
