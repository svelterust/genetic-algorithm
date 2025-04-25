import pygame
from player import Player, JUMP_VELOCITY

WIDTH = 1280
HEIGHT = 720

# Setup PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player
player = Player(100, 100, 64, 64)

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.vspeed = JUMP_VELOCITY

def draw_screen():
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Game logic
    handle_keys()
    player.update()
    draw_screen()
