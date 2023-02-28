# import pygame package
import pygame

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
#screen = pygame.display.set_mode() /sets full window
surface = pygame.display.set_mode((800, 600))
# creating a bool value which checks
# if game is running
color = (255, 0, 0)
surface.fill(color)
pygame.display.flip()

running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False