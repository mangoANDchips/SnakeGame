import pygame

pygame.init()

#GAME CONFIGURATION
TILES = 16
SCALE = 5
ACTUALTILES = TILES * SCALE

#SCREEN CONFIGURATION
SCREEN_HEIGHT = ACTUALTILES * 9
SCREEN_WIDTH =  ACTUALTILES * 16
NAME = 'SNAKE'
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(NAME)

#CHARACTER CONFIGURATION
player = pygame.Rect((0, 0, ACTUALTILES, ACTUALTILES))


run = True
while run:
    SCREEN.fill((255, 255, 255))
    pygame.draw.rect(SCREEN, (0,0,0), player)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()   