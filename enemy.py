import pygame
import time
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_COLOR, ENEMY_WIDTH, ENEMY_HEIGHT
from bullet import Bullet
from collision import check_collision


# Enemy speed
ENEMY_SPEED = 5


# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.direction = 1  # 1 means right, -1 means left
        self.bullets = []
        self.last_shot_time = time.time()  # Initialize last shot time

    def move(self):
        self.rect.x += self.direction * ENEMY_SPEED
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1  # Reverse direction

    def try_to_shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 1:
            self.shoot()
            self.last_shot_time = current_time  # Update last shot time

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.move(dt, 1)
        self.bullets = [
            bullet for bullet in self.bullets if not bullet.is_off_screen(SCREEN_HEIGHT)
        ]

    def draw(self, screen):
        points = [
            (self.rect.left, self.rect.top),
            (self.rect.centerx, self.rect.bottom),
            (self.rect.right, self.rect.top),
        ]
        pygame.draw.polygon(screen, ENEMY_COLOR, points)
        for bullet in self.bullets:
            bullet.draw(screen)

    def check_bullet_collisions(self, player):
        for bullet in self.bullets:
            if check_collision(bullet, player):
                print("Player hit!")
                # Handle player hit logic

    def update(self, dt):
        self.move()
        # self.update_position()
        self.try_to_shoot()
        self.update_bullets(dt)
