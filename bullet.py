import pygame


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = (255, 255, 0)  # Yellow color for the bullet
        self.speed = 500  # pixels per second
        self.shape = "circle"
        self.x = x
        self.y = y
        self.radius = self.rect.width // 2

    def move(self, dt, dir):
        self.rect.move_ip(0, self.speed * dir * dt)
        self.update_position()

    def update_position(self):
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def is_off_screen(self, screen_height):
        return self.rect.bottom < 0
