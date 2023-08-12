import settings
import pygame

class Minesweeper:
    def __init__(self,surface) -> None:
        self._screen = surface

    def initialise_board(self):
        _spacing = settings.SCREEN_SIZE // settings.TILES_NUM
        _y = 0
        for y in range(settings.TILES_NUM):
            _x = 0
            for x in range(settings.TILES_NUM):
                self._screen.blit(pygame.image.load('images/blank_tile.png'),(_x, _y))
                _x += _spacing
            _y += _spacing