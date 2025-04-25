import pygame
from neural_network import NeuralNetwork
from constants import HEIGHT, JUMP_VELOCITY, MAX_VELOCITY, GRAVITY

class Player:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vspeed = 0
        self.color = (0, 0, 0)
        self.outputs = [0.0, 0.0]
        self.neural_network = NeuralNetwork(2, 10, 1)

    def update(self):
        # Physics
        if self.vspeed < MAX_VELOCITY:
            self.vspeed += GRAVITY
        self.y += self.vspeed

        # Neural Network
        self.outputs = self.neural_network.process([
            self.y / HEIGHT,
            (self.vspeed + JUMP_VELOCITY) / MAX_VELOCITY,
        ])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
