import sys
import pygame

# Setup PyGame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player
player = {
    "x": 100,
    "y": 100,
    "width": 64,
    "height": 64,
    "color": BLACK
}

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player["x"] -= 5
    if keys[pygame.K_RIGHT]:
        player["x"] += 5
    if keys[pygame.K_UP]:
        player["y"] -= 5
    if keys[pygame.K_DOWN]:
        player["y"] += 5

def draw_screen():
    pygame.draw.rect(screen, player["color"], (player["x"], player["y"], player["width"], player["height"]))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic
    handle_keys()
    screen.fill(WHITE)
    draw_screen()
    pygame.display.update()
    clock.tick(60)
