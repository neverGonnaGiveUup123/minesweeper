import pygame
import settings as settings
import sys
from core.minesweeper import Minesweeper

def main_loop():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    SCREEN = pygame.display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE + 100))

    game = Minesweeper(SCREEN, settings.TILES_NUM)
    game.initialise_board()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == '__main__':
    main_loop()