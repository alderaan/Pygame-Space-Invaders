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
from collision import check_collision

# Enemy speed
ENEMY_SPEED = 5


# Enemy class
class Enemy:
    def __init__(self, x, y, health=100):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.direction = 1  # 1 means right, -1 means left
        self.bullets = []
        self.last_shot_time = time.time()  # Initialize last shot time
        self.health = health
        self.is_flashing = False
        self.flash_start_time = 0
        self.flash_duration = 0.4  # flash duration in seconds

    def move(self):
        self.rect.x += self.direction * ENEMY_SPEED
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1  # Reverse direction
            self.rect.y += 50

    def try_to_shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= ENEMY_RELOAD_TIME:
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
        if self.is_flashing:
            # Calculate elapsed time since flash started
            elapsed_time = time.time() - self.flash_start_time
            # Determine if we should be showing the original color or white
            if int(elapsed_time * 10) % 2 == 0:
                color = ENEMY_COLOR
            else:
                color = (255, 255, 255)
            # End flashing after the flash duration
            if elapsed_time > self.flash_duration:
                self.is_flashing = False
        else:
            color = ENEMY_COLOR

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
