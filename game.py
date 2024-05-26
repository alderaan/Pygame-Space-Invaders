import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from collision import check_collision


def run_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    enemies = [Enemy(100, 100), Enemy(200, 100), Enemy(300, 100)]

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

        # update player
        player.update(dt, keys)

        # update enemies
        for enemy in enemies:
            enemy.update(dt)
            # enemy.check_bullet_collisions(player)

        # Check if player's bullets hit enemies
        for bullet in player.bullets[:]:  # Iterate over a copy of the list
            for enemy in enemies[:]:  # Iterate over a copy of the list
                if check_collision(bullet, enemy):
                    if enemy.take_damage(25):
                        enemies.remove(enemy)
                    player.bullets.remove(bullet)
                    break

        # Check if enemy bullets hit the player
        for enemy in enemies:
            for bullet in enemy.bullets:
                if check_collision(bullet, player):
                    print("Player hit!")
                    # Handle player hit logic
                    enemy.bullets.remove(bullet)
                    # Optionally, reduce player's health or handle game over

        # RENDERING
        screen.fill((0, 0, 0))
        player.draw(screen)
        for enemy in enemies:  # Corrected: Draw each enemy
            enemy.draw(screen)
        pygame.display.update()

    pygame.quit()
