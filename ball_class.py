import pygame


class Ball:
    VEL = 6
    COLOR = (255, 255, 255)

    def __init__(self, x, y, radius):
        self.x = self.start_x = x
        self.y = self.start_y = y
        self.radius = radius

        # first move during initialization
        self.x_vel = self.VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.x_vel *= -1
        self.y_vel = 0