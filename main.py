import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up a clock to manage frame rate
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 250, 50, 50))
speed = 600  # pixels per second

color_1 = (255, 0, 0)
color_2 = (0, 255, 0)
color_3 = (0, 0, 255)
color_4 = (255, 255, 255)

player_color = color_1

run = True
while run:

    # Calculate delta time
    dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, player_color, player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-speed * dt, 0)
        player_color = color_1
    elif key[pygame.K_d]:
        player.move_ip(speed * dt, 0)
        player_color = color_2
    elif key[pygame.K_w]:
        player.move_ip(0, -speed * dt)
        player_color = color_3
    elif key[pygame.K_s]:
        player.move_ip(0, speed * dt)
        player_color = color_4

    # Ensure the player stays within screen boundaries
    if player.left < 0:
        player.left = 0
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
