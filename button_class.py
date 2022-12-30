import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Button")
text_font = pygame.font.SysFont("comicsans", 50)


class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.8), int(height * 0.8)))
        self.x = x_pos
        self.y = y_pos
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_input = text_input
        self.text = text_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.text_rect)

        return action
