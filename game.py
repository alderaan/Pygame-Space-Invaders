import pygame
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPAWN_INTERVAL
from enemy import Enemy
from collision import check_collision


def run_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    enemies = [
        Enemy(100, 0),
        Enemy(300, 0),
        Enemy(500, 0),
    ]

    spawn_timer = 0
    spawn_interval = ENEMY_SPAWN_INTERVAL

    run = True

    # GAME LOOP
    while run:
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        spawn_timer += dt

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

        # Check if player's bullets hit enemies
        for bullet in player.bullets[:]:
            for enemy in enemies[:]:
                if check_collision(bullet, enemy):
                    if enemy.take_damage(25):
                        enemies.remove(enemy)
                    player.bullets.remove(bullet)
                    break

        # Check if enemy bullets hit the player
        for enemy in enemies[:]:
            for bullet in enemy.bullets[:]:
                if check_collision(bullet, player):
                    if player.take_damage(25):
                        print("Player hit!")
                    enemy.bullets.remove(bullet)
                    # Optionally, reduce player's health or handle game over

        # Spawn a new enemy every x seconds
        if spawn_timer >= spawn_interval:
            enemies.extend(
                [
                    Enemy(100, 0),
                    Enemy(300, 0),
                    Enemy(500, 0),
                ]
            )
            spawn_timer = 0  # Reset the spawn timer

        # RENDERING
        screen.fill((0, 0, 0))
        player.draw(screen)
        for enemy in enemies:  # Corrected: Draw each enemy
            enemy.draw(screen)
        pygame.display.update()

    pygame.quit()
