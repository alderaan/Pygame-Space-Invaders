import pygame
import time
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_COLOR, ENEMY_WIDTH, ENEMY_HEIGHT
from bullet import Bullet


# Enemy speed
ENEMY_SPEED = 5


# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.direction = 1  # 1 means right, -1 means left
        self.bullets = []
        self.last_shot_time = time.time()  # Initialize last shot time

    def move(self):
        self.x += self.direction * ENEMY_SPEED
        if self.x + self.width >= SCREEN_WIDTH or self.x <= 0:
            self.direction *= -1  # Reverse direction

    def try_to_shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 1:
            self.shoot()
            self.last_shot_time = current_time  # Update last shot time

    def shoot(self):
        bullet = Bullet(self.x, self.y)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.move(dt, 1)
        self.bullets = [
            bullet for bullet in self.bullets if not bullet.is_off_screen(SCREEN_HEIGHT)
        ]

    def draw(self, screen):
        points = [
            (self.x, self.y),
            (self.x + self.width // 2, self.y + self.height),
            (self.x + self.width, self.y),
        ]
        pygame.draw.polygon(screen, ENEMY_COLOR, points)
        for bullet in self.bullets:
            bullet.draw(screen)

    def update(self, dt):
        self.move()
        self.try_to_shoot()
        self.update_bullets(dt)
