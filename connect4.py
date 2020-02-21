import pygame
import random
from colors import *

pygame.init()

size = (310, 310)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
finished = False

slots = []

x_list = [5, 55, 105, 155, 205, 255, 305]

def draw_background():
  for i in range 42:
    
