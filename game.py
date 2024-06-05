import pygame
import time
from player import Player
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_SPAWN_INTERVAL,
    ENEMY_SPEED,
    ENEMY_RELOAD_TIME,
    PLAYER_BULLET_DAMAGE,
    BLACK,
    WHITE,
)
from enemy import Enemy
from collision import check_collision


def game_over_screen(screen):
    font = pygame.font.Font(None, 74)
    screen.fill(BLACK)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)


def initialize_game():
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    enemies = []
    spawn_timer = 0
    score = 0
    return player, enemies, spawn_timer, score


def run_game():
    pygame.init()
    pygame.display.set_caption("David's Space Invaders")

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        player, enemies, spawn_timer, score = initialize_game()
        game_over = False
        enemy_speed_mod = 1.0
        enemy_reload_mod = 1.0

        while not game_over:
            dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
            spawn_timer += dt

            # EVENT HANDLING
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.shoot()

            keys = pygame.key.get_pressed()

            # Update player
            player.update(dt, keys)

            # Update enemies
            for enemy in enemies:
                enemy.update(dt)

            # Check if player's bullets hit enemies
            for bullet in player.bullets[:]:
                for enemy in enemies[:]:
                    if check_collision(bullet, enemy):
                        if enemy.take_damage(PLAYER_BULLET_DAMAGE):
                            enemies.remove(enemy)
                            score += 1  # Increment score when an enemy is killed
                        player.bullets.remove(bullet)
                        break

            # Check if enemy bullets hit the player
            for enemy in enemies[:]:
                for bullet in enemy.bullets[:]:
                    if check_collision(bullet, player):
                        if player.take_damage(25):
                            game_over_screen(screen)
                            game_over = True
                        enemy.bullets.remove(bullet)

            # Spawn a new enemy every x seconds
            if spawn_timer >= ENEMY_SPAWN_INTERVAL:
                enemy_speed_mod += 0.1
                enemy_reload_mod -= 0.05
                if enemy_reload_mod <= 0.3:
                    enemy_reload_mod = 0.3
                print(ENEMY_SPEED * enemy_speed_mod)
                enemies.append(
                    Enemy(
                        0,
                        0,
                        health=100,
                        speed=ENEMY_SPEED * enemy_speed_mod,
                        reload_time=ENEMY_RELOAD_TIME * enemy_reload_mod,
                    )
                )
                spawn_timer = 0  # Reset the spawn timer

            # RENDERING
            screen.fill((0, 0, 0))
            player.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)

            # Display the score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))  # Top-left corner

            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    run_game()
