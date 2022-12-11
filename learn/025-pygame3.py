# ----------------------------------
# This script is used for learning python
# Now we will try to smooth moving of our picture
# Base script is written in file 024-*
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
import pygame
# set screen size
max_x = 800
max_y = 600
# set variable for image size, x and y can be defined separately
image_size = 150
pygame.init()
# create a screen
# use a fullscreen - pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN)
screen = pygame.display.set_mode((max_x, max_y))
# define title of the screen
pygame.display.set_caption("python_lesson")
# check if pygame support different picture types - png, jpeg etc.
print(pygame.image.get_extended())
# load image to variable
image1 = pygame.image.load('picture2.jpg')
# next we want to resize image to be smaller than original
image1 = pygame.transform.scale(image1, (image_size, image_size))
# game_over used to stop execution of the script
game_over = False
# x and y - initial picture position
x = 250
y = 100
# lets define background color
bg_color = ( 0,100,0 )
# lets define initial moving state to False
move_right = False
move_left = False
move_up = False
move_down = False

while game_over == False:
    # read all events in pygame, like mouse clicking or pressing buttons
    for event in pygame.event.get():
        # tracking any button pressing down
        if event.type == pygame.KEYDOWN:
            # stop the loop on ESC button
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        # define what to do on unpressing the button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
    # define what to do if variables set to True
    if move_left == True:
        x -= 1
        # stop moving on the edge of the screen
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        # stop moving on the edge of the screen
        if x > max_x - image_size:
            x = max_x - image_size
    if move_up == True:
        y -= 1
        # stop moving on the edge of the screen
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        # stop moving on the edge of the screen
        if y > max_y - image_size:
            y = max_y - image_size
    # make background color
    screen.fill(bg_color)
    # show the picture
    screen.blit(image1, (x, y))
    pygame.display.flip()
