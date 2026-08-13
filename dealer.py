import pygame

class Dealer:
    def __init__(self):
        self.width = 64
        self.height = 100
        self.x = 368
        self.y = 440
        self.change_x = 0
        self.change_y = 0
        self.velocity = 0.5
        self.image = pygame.image.load("dealer.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen_surface):
        screen_surface.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.width:
            self.x = 800 - self.width

        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.height:
            self.y = 600 - self.height

    def move_left(self):
        self.change_x = -self.velocity

    def move_right(self):
        self.change_x = self.velocity

    def move_up(self):
        self.change_y = -self.velocity

    def move_down(self):
        self.change_y = self.velocity

    def stop_horizontal(self):
        self.change_x = 0

    def stop_vertical(self):
        self.change_y = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_center_x(self):
        return self.x + self.width / 2

    def get_center_y(self):
        return self.y + self.height / 2
