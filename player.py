import pygame
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
from collision import check_collision


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = PLAYER_COLOR
        self.bullets = []

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

    # def draw(self, screen):
    #    pygame.draw.rect(screen, self.color, self.rect)
    #    for bullet in self.bullets:
    #        bullet.draw(screen)

    def draw(self, screen):
        points = [
            (self.rect.left, self.rect.bottom),  # Bottom-left corner
            (self.rect.centerx, self.rect.top),  # Top-center
            (self.rect.right, self.rect.bottom),  # Bottom-right corner
        ]
        pygame.draw.polygon(screen, PLAYER_COLOR, points)
        for bullet in self.bullets:
            bullet.draw(screen)

    def update(self, dt, keys):
        self.move(dt, keys)
        self.update_bullets(dt)
