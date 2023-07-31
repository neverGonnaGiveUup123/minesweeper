import pygame
import settings
import sys
import json
import math
import time
from random import randint


class Minesweeper:
    def __init__(self) -> None:
        self._screen_dimensions = settings.SCREEN_DIMENSIONS
        self._fps = settings.FPS
        self._caption = settings.CAPTION
        self._grid_size = settings.GRID_SIZE
        self._x_coords = ("1", "2", "3", "4", "5")
        self._y_coords = ("1", "2", "3", "4", "5")
        self._num_of_mines = settings.MAX_NUM_OF_MINES
        self._images = settings.IMAGES

    def initialise_board(self):
        for _ in range(self._grid_size**2):
            for x in self._x_coords:
                for y in self._y_coords:
                    with open(f"tiles/tile{x}{y}.json", "w") as file:
                        json.dump({"num_of_mines": 0, "mine": False, 'assigned_tile' : self._images['blank_tile']}, file)

    def set_mines(self):
        mined_tiles = []
        for _ in range(self._num_of_mines):
            mined_tiles.append((randint(1, 5), randint(1, 5)))
        for x, y in set(mined_tiles):
            with open(f"tiles/tile{x}{y}.json", "r") as file:
                mine_data = json.load(file)
            mine_data["mine"] = True
            with open(f"tiles/tile{x}{y}.json", "w") as file:
                json.dump(mine_data, file)
    
    def mouse_func(self, screen):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        screen.blit(pygame.image.load(self._images['hover_tile']), (self.roundup(x) - 100, self.roundup(y) - 100))

        if pygame.mouse.get_pressed()[0] == True:
            time.sleep(0.1)
            print(self.roundup(x)), print(self.roundup(y))
    
    def get_assigned_tile(self):
        for _ in range(self._grid_size**2):
            for x in self._x_coords:
                for y in self._y_coords:
                    with open(f"tiles/tile{x}{y}.json", "r") as file:
                        return json.load(file)['assigned_tile']

    def mainloop(self) -> None:
        pygame.init()
        pygame.display.set_caption(self._caption)
        SCREEN = pygame.display.set_mode(self._screen_dimensions)

        while True:
            y = 0
            for __ in range(5):
                x = 0
                for _ in range(5):
                    
                    SCREEN.blit(pygame.image.load(self.get_assigned_tile()), (x,y))
                    x += 100
                y += 100
            self.mouse_func(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
    
    @staticmethod
    def roundup(x):
        return int(math.ceil(x / 100.0)) * 100


e = Minesweeper()
e.initialise_board()
e.set_mines()
e.mainloop()
