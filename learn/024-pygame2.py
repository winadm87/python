# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import pygame
# set screen size
max_x = 800
max_y = 600
pygame.init()
# create a screen
# use a fullscreen - pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN)
screen = pygame.display.set_mode((max_x, max_y))
# define title of the screen
pygame.display.set_caption("python_lesson")
# check if pygame support different picture types - png, jpeg etc.
print(pygame.image.get_extended())
# load image to variable
image1 = pygame.image.load('picture1.jpg')
# next we want to resize image to be smaller than original
image1 = pygame.transform.scale(image1, (100, 100))
game_over = False
x = 250
y = 100
bg_color = ( 0,100,0 )
while game_over == False:
    # read all events in pygame, like mouse clicking or pressing buttons
    for event in pygame.event.get():
        # tracking any button pressing down
        if event.type == pygame.KEYDOWN:
            # stop the loop on ESC button
            # or move out picture on arrow keys
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        # also we want to track mouse clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    # make background color
    screen.fill(bg_color)
    # show the picture
    screen.blit(image1, (x, y))
    pygame.display.flip()