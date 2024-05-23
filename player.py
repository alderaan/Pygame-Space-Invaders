import pygame
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SPEED,
    COLOR_1,
    COLOR_2,
    COLOR_3,
    COLOR_4,
)


class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = COLOR_1

    def move(self, dt, keys):
        if keys[pygame.K_a]:
            self.rect.move_ip(-SPEED * dt, 0)
            self.color = COLOR_1
        elif keys[pygame.K_d]:
            self.rect.move_ip(SPEED * dt, 0)
            self.color = COLOR_2
        elif keys[pygame.K_w]:
            self.rect.move_ip(0, -SPEED * dt)
            self.color = COLOR_3
        elif keys[pygame.K_s]:
            self.rect.move_ip(0, SPEED * dt)
            self.color = COLOR_4

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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
