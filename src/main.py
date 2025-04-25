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
    "color": BLACK,
    "vspeed": 0
}

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player["vspeed"] = -13

def draw_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, player["color"], (player["x"], player["y"], player["width"], player["height"]))
    pygame.display.update()
    clock.tick(60)

def update_player():
    player["vspeed"] += 0.75
    player["y"] += player["vspeed"]

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic
    handle_keys()
    update_player()
    draw_screen()
