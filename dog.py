import pygame
import random
from enemy import Enemy


class Dog(Enemy):
    def __init__(self):
        image = pygame.image.load("dog.png")
        image = pygame.transform.scale(image, (54, 64))

        x, y = random.choice([
            [random.randint(0, 746), -64],
            [random.randint(0, 746), 600],
            [-54, random.randint(0, 536)],
            [800, random.randint(0, 536)]
        ])

        super().__init__(x, y, image, 54, 64, 0.25, 3)