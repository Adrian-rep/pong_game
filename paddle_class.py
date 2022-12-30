import pygame


class Paddles:
    VEL = 6
    COLOR = (255, 255, 255)

    def __init__(self, x, y, width, height):
        self.x = self.start_x = x
        self.y = self.start_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=False):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
