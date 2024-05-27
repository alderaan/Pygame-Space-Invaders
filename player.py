import pygame
import time
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
    PLAYER_COLOR,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_BULLET_COLOR,
)
from bullet import Bullet

# from collision import check_collision
from flashing_effect import get_flash_color


class Player:
    def __init__(self, x, y, health=100):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = PLAYER_COLOR
        self.bullets = []
        self.health = health
        self.is_flashing = False
        self.flash_start_time = 0
        self.flash_duration = 0.4

    def move(self, dt, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED * dt, 0)
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED * dt, 0)

        self.check_bounds()

    def check_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, PLAYER_BULLET_COLOR)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.move(dt, -1)
        self.bullets = [
            bullet for bullet in self.bullets if not bullet.is_off_screen(SCREEN_HEIGHT)
        ]

    def take_damage(self, damage):
        print("Player took damage")
        self.health -= damage
        if self.health <= 0:
            print("Player died")
            return True  # Enemy is dead
        # Start flashing
        self.is_flashing = True
        self.flash_start_time = time.time()
        return False

    def draw(self, screen):
        color, self.is_flashing = get_flash_color(
            self.is_flashing,
            self.flash_start_time,
            PLAYER_COLOR,
            (255, 0, 0),
            self.flash_duration,
        )

        points = [
            (self.rect.left, self.rect.bottom),  # Bottom-left corner
            (self.rect.centerx, self.rect.top),  # Top-center
            (self.rect.right, self.rect.bottom),  # Bottom-right corner
        ]
        pygame.draw.polygon(screen, color, points)
        for bullet in self.bullets:
            bullet.draw(screen)

    def update(self, dt, keys):
        self.move(dt, keys)
        self.update_bullets(dt)
