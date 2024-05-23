import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT


def run_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(350, 250, 50, 50)

    run = True
    while run:
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()

        keys = pygame.key.get_pressed()
        player.move(dt, keys)
        player.update_bullets(dt)

        screen.fill((0, 0, 0))
        player.draw(screen)

        pygame.display.update()

    pygame.quit()
