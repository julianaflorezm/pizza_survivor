import pygame
import random
from enemy import Enemy


class Cat(Enemy):
    def __init__(self):
        width = 44
        height = 52
        image = pygame.image.load("cat.png")
        image = pygame.transform.scale(image, (width, height))

        x, y = random.choice([
            [random.randint(0, 800 - width), -height],
            [random.randint(0, 800 - width), 600],
            [-width, random.randint(0, 600 - height)],
            [800, random.randint(0, 600 - height)]
        ])

        super().__init__(x, y, image, width, height, 0.25, 3)
