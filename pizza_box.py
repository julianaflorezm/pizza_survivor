import random
import pygame


class PizzaBox:
    def __init__(self):
        self.width = 45
        self.height = 45

        self.image = pygame.image.load("pizza.png")
        self.image = pygame.transform.scale(
            self.image,
            (self.width, self.height)
        )

        self.x = random.randint(0, 800 - self.width)
        self.y = random.randint(0, 600 - self.height)

        self.creation_time = pygame.time.get_ticks()
        self.duration = 5000  # 5 segundos

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def has_expired(self, current_time):
        return current_time - self.creation_time >= self.duration

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))