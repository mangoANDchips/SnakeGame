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
X = 0
Y = 0
SPEED = 5
player = pygame.Rect((X, Y, ACTUALTILES, ACTUALTILES))


run = True
while run:
    pygame.time.delay(10)
    SCREEN.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    press = pygame.key.get_pressed()
    
    #MOVEMENT
    if press[pygame.K_a]:
        player.x -= SPEED
    if press[pygame.K_d]:
        player.x += SPEED        
    if press[pygame.K_w]:   
        player.y -= SPEED
    if press[pygame.K_s]:    
        player.y += SPEED
    
    pygame.draw.rect(SCREEN, (0,0,0), player)
    pygame.display.update()
pygame.quit()   