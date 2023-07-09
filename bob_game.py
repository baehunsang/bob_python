import sys
import os
import pygame
from pygame.locals import QUIT, KEYDOWN
import random
import math

MAX_X_INDEX = 9
MAX_Y_INDEX = 19

BLOCK_COLORS = [
    (64, 64, 64),
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (128, 0, 0),
    (0, 128, 0),
    (0, 0, 128),
    (255, 0, 255),
    (0, 255, 255),
]

SCREEN_SIZE = {
    'width' : 240,
    'height' : 400
}

def get_initialized_board():
    board = []
    for _ in range(0, 20):
        board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    return board

class Block:
    def __init__(self) -> None:
        self.position = {
            'x' : 5,
            'y' : 2
        }
        self.bricks = []
    
    def init_position(self):
        self.position = {
            'x' : 5,
            'y' : 2
        }

    def move_left(self):
        self.position['x'] -= 1

    def move_right(self):
        self.position['x'] += 1

    def move_down(self):
        self.position['y'] += 1

    def change(self):
        tmp = self.bricks[0]
        self.bricks[0] = self.bricks[1]
        self.bricks[1] = self.bricks[2]
        self.bricks[2] = tmp

    
    
    


def main():
    pygame.init()

    screen= pygame.display.set_mode((SCREEN_SIZE['width'], SCREEN_SIZE['height']))
    pygame.display.set_caption("HEXA")

    #Initialize Game Object
    now_block = Block()
    next_block = Block()
    board = get_initialized_board()

    #Initialize Blocks with random colors
    now_block.bricks = [
        random.randint(1, len(BLOCK_COLORS) - 1),
        random.randint (1, len(BLOCK_COLORS) - 1),
        random.randint(1, len(BLOCK_COLORS) - 1),
    ]
    next_block.init_position()
    next_block.bricks = [
        random.randint(1, len(BLOCK_COLORS) - 1),
        random.randint (1, len(BLOCK_COLORS) - 1),
        random.randint(1, len(BLOCK_COLORS) - 1),
    ]


    pygame.quit()
if __name__ == '__main__':
    main()