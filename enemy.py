import pygame
import time
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_COLOR,
    ENEMY_WIDTH,
    ENEMY_HEIGHT,
    ENEMY_BULLET_COLOR,
    ENEMY_RELOAD_TIME,
)
from bullet import Bullet
from flashing_effect import get_flash_color


# Enemy class
class Enemy:
    def __init__(self, x, y, health=100, speed=5, reload_time=1):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.direction = 1  # 1 means right, -1 means left
        self.bullets = []
        self.last_shot_time = time.time()  # Initialize last shot time
        self.health = health
        self.speed = speed
        self.reload_time = reload_time
        self.is_flashing = False
        self.flash_start_time = 0
        self.flash_duration = 0.4

    def move(self):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1  # Reverse direction
            self.rect.y += 50

    def try_to_shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.reload_time:
            self.shoot()
            self.last_shot_time = current_time  # Update last shot time

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom, ENEMY_BULLET_COLOR)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.move(dt, 1)
        self.bullets = [
            bullet for bullet in self.bullets if not bullet.is_off_screen(SCREEN_HEIGHT)
        ]

    def draw(self, screen):
        color, self.is_flashing = get_flash_color(
            self.is_flashing,
            self.flash_start_time,
            ENEMY_COLOR,
            (255, 255, 255),
            self.flash_duration,
        )
        points = [
            (self.rect.left, self.rect.top),
            (self.rect.centerx, self.rect.bottom),
            (self.rect.right, self.rect.top),
        ]
        pygame.draw.polygon(screen, color, points)
        for bullet in self.bullets:
            bullet.draw(screen)

    def take_damage(self, damage):
        print("Enemy took damage")
        self.health -= damage
        if self.health <= 0:
            print("Enemy died")
            return True  # Enemy is dead
        # Start flashing
        self.is_flashing = True
        self.flash_start_time = time.time()
        return False

    def update(self, dt):
        self.move()
        self.try_to_shoot()
        self.update_bullets(dt)
