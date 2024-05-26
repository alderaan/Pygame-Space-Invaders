import pygame
from config import BULLET_SPEED


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = (255, 255, 0)  # Yellow color for the bullet
        self.speed = BULLET_SPEED  # pixels per second
        self.radius = self.rect.width // 2

    def move(self, dt, dir):
        self.rect.move_ip(0, self.speed * dir * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def is_off_screen(self, screen_height):
        return self.rect.bottom < 0
