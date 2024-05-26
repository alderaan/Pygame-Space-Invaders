import pygame
from config import BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT


class Bullet:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.color = color
        self.speed = BULLET_SPEED
        self.radius = self.rect.width // 2

    def move(self, dt, dir):
        self.rect.move_ip(0, self.speed * dir * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def is_off_screen(self, screen_height):
        return self.rect.bottom < 0
