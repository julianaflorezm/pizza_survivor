import pygame

class Enemy:
    def __init__(self, x, y, image, width, height, velocity, lives):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.velocity = velocity
        self.lives = lives

    def draw(self, screen_surface):
        screen_surface.blit(self.image, (self.x, self.y))

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > 0:
            self.x += (dx / distance) * self.velocity
            self.y += (dy / distance) * self.velocity

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_center_x(self):
        return self.x + self.width / 2

    def get_center_y(self):
        return self.y + self.height / 2

    def distance_to(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def receive_damage(self):
        self.lives -= 1

    def is_dead(self):
        return self.lives <= 0