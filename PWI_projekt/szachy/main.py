import pygame as pg
from game.board import *
from game.game import *
from game.options import Menu
from time import *
from game.DumbBot import *
from game.players import *


pg.init()

def main():
    menu = Menu()
    selected_option = menu.run()

    if (selected_option == "Player vs Player"
            or selected_option == "Player vs Bot - White - Dumb Bot" or selected_option == "Player vs Bot - White - Smart Bot"
        or selected_option == "Player vs Bot - Black - Dumb Bot" or selected_option == "Player vs Bot - White - Dumb Bot"):


        screen_size = 800
        screen = pg.display.set_mode((screen_size, screen_size))
        pg.display.set_caption("Szachy")
        white = (220, 230, 255)
        brown = (205, 133, 63)
        board = ChessBoard(screen_size, (white, brown), screen)




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
        screen_size = 800
        screen = pg.display.set_mode((screen_size, screen_size))
        pg.display.set_caption("Szachy")
        white = (220, 230, 255)
        brown = (205, 133, 63)
        board = ChessBoard(screen_size, (white, brown), screen)

        bot1 = DumbBot("w")
        bot2 = DumbBot("b")

        game = Game(board, bot1, bot2)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break

            screen.fill((0, 0, 0))
            board.draw_board()
            board.draw_pieces()

            if game.current_turn == "w":
                time.sleep(2)  # Wait 2 seconds before making a move for better visibility
                bot1.make_move(board)
            else:
                time.sleep(2)  # Wait 2 seconds before making a move for better visibility
                bot2.make_move(board)

            pg.display.flip()


if __name__ == "__main__":
    main()
