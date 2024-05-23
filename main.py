import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 250, 50, 50))

color_1 = (255, 0, 0)
color_2 = (0, 255, 0)
color_3 = (0, 0, 255)
color_4 = (255, 255, 255)

player_color = color_1

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, player_color, player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
        player_color = color_1
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
        player_color = color_2
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
        player_color = color_3
    elif key[pygame.K_s]:
        player.move_ip(0, 1)
        player_color = color_4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
