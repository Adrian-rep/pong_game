import time
import pygame
import random
from game_functions import Game
from paddle_class import Paddles
from ball_class import Ball
from button_class import Button


def main():
    pygame.init()
    game = Game()

    while True:
        menu_screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
        menu_screen.fill(game.BLACK)
        pygame.display.set_caption('Menu')

        # load button images
        start_img = pygame.image.load('button.png')
        exit_img = pygame.image.load('button.png')

        # create button instances
        start_button = Button(start_img, game.WIDTH / 4, game.HEIGHT / 2, 'PLAY')
        exit_button = Button(exit_img, 3 * game.WIDTH / 4, game.HEIGHT / 2, 'QUIT')

        if start_button.draw(menu_screen):
            game_screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
            pygame.display.set_caption("PONG")
            loop = game.game_loop(game_screen)

            if not loop:
                main()
        if exit_button.draw(menu_screen):
            exit()
            break
        pygame.display.update()


if __name__ == "__main__":
    main()
