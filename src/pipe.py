import random
import pygame
from neural_network import NeuralNetwork
from constants import WIDTH, HEIGHT, GAP_SIZE, PIPE_MOVE_SPEED

class Pipe:
    def __init__(self):
        self.width = 128
        self.height = 256
        self.gap_size = GAP_SIZE

        # Randomize the gap position (can be closer to top or bottom)
        self.x = WIDTH
        self.y = random.randint(100, HEIGHT - 100 - self.gap_size)

        # Define the top and bottom pieces
        self.top_height = self.y
        self.bottom_y = self.y + self.gap_size
        self.bottom_height = HEIGHT - self.bottom_y

    def update(self):
        self.x -= PIPE_MOVE_SPEED

    def draw(self, screen):
        # Draw top pipe (upside down)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.top_height))

        # Draw bottom pipe
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.bottom_y, self.width, self.bottom_height))
