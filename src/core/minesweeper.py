import settings as settings
import pygame
import json
from core.mine import Mine
from random import randint

class Minesweeper:
    def __init__(self,surface,tiles) -> None:
        self._screen = surface
        self._tiles_num = tiles

    def initialise_board(self):
        _spacing = settings.SCREEN_SIZE // self._tiles_num
        _y = 0
        for y in range(self._tiles_num):
            _x = 0
            for x in range(self._tiles_num):
                self._screen.blit(pygame.image.load('images/blank_tile.png'),(_x, _y))
                _x += _spacing
            _y += _spacing
        
        mines_coords = []
        [mines_coords.append((randint(1,self._tiles_num), randint(1, self._tiles_num))) for i in range(settings.MAX_MINES_COUNT)]
        print(set(mines_coords))