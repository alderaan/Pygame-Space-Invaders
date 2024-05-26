import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy


def run_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    enemy = Enemy(SCREEN_WIDTH // 2, 50)

    run = True

    # GAME LOOP
    while run:
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()

        keys = pygame.key.get_pressed()

        player.update(dt, keys)
        enemy.update(dt)

        # Check if enemy bullets hit the player
        enemy.check_bullet_collisions(player)

        # RENDERING
        screen.fill((0, 0, 0))
        player.draw(screen)
        enemy.draw(screen)
        pygame.display.update()

    pygame.quit()
