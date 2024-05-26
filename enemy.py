import pygame
from config import SCREEN_WIDTH

SCREEN_HEIGHT = 600

# Colors
ENEMY_COLOR = (255, 0, 0)


# Enemy speed
ENEMY_SPEED = 5


# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.direction = 1  # 1 means right, -1 means left

    def move(self):
        self.x += self.direction * ENEMY_SPEED
        if self.x + self.width >= SCREEN_WIDTH or self.x <= 0:
            self.direction *= -1  # Reverse direction

    def draw(self, screen):
        points = [
            (self.x, self.y),
            (self.x + self.width // 2, self.y - self.height),
            (self.x + self.width, self.y),
        ]
        pygame.draw.polygon(screen, ENEMY_COLOR, points)
