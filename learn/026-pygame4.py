# ----------------------------------
# This script is used for learning python
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import pygame
import random
import sys
# define screen size
max_x = 800
max_y = 800
# define snow quantity and size
max_snow = 100
snow_size = 64

class snow():
    """class for snow"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # slightly random speed of snoflakes
        self.speed = random.randint(1, 3) # random speed for snowflakes
        self.img_num = random.randint(1, 4) # we have 4 pictures
        # define pictures in the same folder
        self.image_filename = "snowflake" + str(self.img_num) + ".png"
        # load images
        self.image = pygame.image.load(self.image_filename).convert()
        # convert snowflake image to required size
        self.image = pygame.transform.scale(self.image, (snow_size, snow_size))
    def move_snow(self):
        # move down
        self.y = self.y + self.speed
        # after bottom - goes from top
        if self.y - max_y:
            self.y = (0 - snow_size)
        i = random.randint(1, 3)
        if i == 1: # move right
            self.x = self.x + 1
            if self.x > max_x:
                self.x = (0 - snow_size)
        elif i == 2: # move left
            self.x = self.x - 1
            if self.x < (0 - snow_size):
                self.x = max_x
    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        # define default snowflake position
        xx = random.randint(0, max_x)
        yy = random.randint(0, max_y)
        # add snoflake to array
        snowfall.append(snow(xx, yy))
def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
# -------- main -------------

pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
bg_color = ( 0,0,0 )
snowfall = []

initialize_snow(max_snow, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    pygame.display.flip()