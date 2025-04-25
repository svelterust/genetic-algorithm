import math
import random
import pygame

def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))

class Node:
    def __init__(self, amount_weights: int):
        self.data = 0.0
        self.bias = 0.0
        self.weights = [random.uniform(-1, 1) for _ in range(amount_weights)]

def create_layer(current_layer_size: int, next_layer_size: int):
    return [Node(next_layer_size) for _ in range(current_layer_size)]

class NeuralNetwork:
    def __init__(self, inputs_size: int, hiddens_size: int, outputs_size: int):
        self.layers = [
            create_layer(inputs_size, hiddens_size),
            create_layer(hiddens_size, outputs_size),
            create_layer(outputs_size, 0)
        ]

    def process(self, inputs: list[float]) -> list[float]:
        # Set values
        for node, value in zip(self.layers[0], inputs):
            node.data = value

        # Forward data
        for i in range(1, len(self.layers)):
            # Get layers
            current_layer = self.layers[i]
            previous_layer = self.layers[i - 1]

            # Forward data
            for node in current_layer:
                node.data = sum(node.weights[j] * previous_layer[j].data for j in range(len(previous_layer))) + node.bias
                node.data = sigmoid(node.data)

        # Return data
        return [node.data for node in self.layers[-1]]
