import pygame


class Pizza:
    def __init__(self, x, y, change_x, change_y):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("pizza.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen_surface):
        screen_surface.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def is_inside_screen(self):
        return -self.width <= self.x <= 800 and -self.height <= self.y <= 600

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
