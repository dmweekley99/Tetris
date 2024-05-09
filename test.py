from grid import Grid
import pygame
from blocks import LBlock

pygame.init()
dark_blue = (44, 44, 127)

# game display size
screen = pygame.display.set_mode((300, 600))

# title of game
pygame.display.set_caption("Python Tetris")

game_grid = Grid()

block = LBlock()

game_grid.print_grid()