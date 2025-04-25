import pygame
from pipe import Pipe
from player import Player
from constants import WIDTH, HEIGHT, JUMP_VELOCITY

# Setup PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Objects
pipes = [Pipe()]
player = Player(100, 100, 64, 64)

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.vspeed = JUMP_VELOCITY

def update():
    player.update()
    for pipe in pipes:
        pipe.update()

def draw_screen():
    screen.fill((0, 0, 0))
    player.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    pygame.display.update()
    clock.tick(60)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Game logic
    handle_keys()
    update()
    draw_screen()
