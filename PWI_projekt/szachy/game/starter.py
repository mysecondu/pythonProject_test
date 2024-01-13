# starter.py
import pygame as pg
from board import ChessBoard
from PWI_projekt.szachy.game.pieces.king import King
from PWI_projekt.szachy.game.pieces.queen import Queen
from PWI_projekt.szachy.game.pieces.rook import Rook
from PWI_projekt.szachy.game.pieces.bishop import Bishop
from PWI_projekt.szachy.game.pieces.knight import Knight
from PWI_projekt.szachy.game.pieces.pawn import Pawn

# Initialize Pygame
pg.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
FONT_SIZE = 36

# Function to display text on the screen
def draw_text(surface, text, size, x, y, color):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

# Main function to start the game
def start_game():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Chess Game - Starter Screen")

    clock = pg.time.Clock()

    running = True
    player_color = None
    bot_difficulty = None

    while running:
        screen.fill(BLACK)

        draw_text(screen, "Chess Game", 2 * FONT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, LIGHT_BLUE)
        draw_text(screen, "Player vs Player", FONT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, LIGHT_BLUE)
        draw_text(screen, "Player vs Bot", FONT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + FONT_SIZE, LIGHT_BLUE)
        draw_text(screen, "Bot vs Bot", FONT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 2 * FONT_SIZE, LIGHT_BLUE)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if SCREEN_WIDTH // 4 < pos[0] < 3 * SCREEN_WIDTH // 4:
                    if SCREEN_HEIGHT // 2 < pos[1] < SCREEN_HEIGHT // 2 + FONT_SIZE:
                        ChessBoard.player_vs_player()
                        running = False
                    elif SCREEN_HEIGHT // 2 + FONT_SIZE < pos[1] < SCREEN_HEIGHT // 2 + 2 * FONT_SIZE:
                        player_color = input("Choose color (black or white): ")
                        bot_choice = input("Choose bot difficulty (dumb or smart): ")
                        ChessBoard.player_vs_bot(player_color, bot_choice)
                        running = False
                    elif SCREEN_HEIGHT // 2 + 2 * FONT_SIZE < pos[1] < SCREEN_HEIGHT // 2 + 3 * FONT_SIZE:
                        ChessBoard.bot_vs_bot()
                        running = False

        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    start_game()
