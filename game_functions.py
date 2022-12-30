import pygame
from paddles_class1 import Paddles
from ball_class1 import Ball
pygame.init()


class Game:
    font = pygame.font.SysFont("comicsans", 32)
    sound = pygame.mixer.Sound("bounce.wav")

    def __init__(self):
        self.WIDTH = 700
        self.HEIGHT = 500
        self.PADDLE_WIDTH = 15
        self.PADDLE_HEIGHT = 100
        self.RADIUS = 7
        self.FPS = 50
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.WIN_SCORE = 1
        self.left_score, self.right_score = 0, 0

    def collisions(self, left_paddle, right_paddle, ball):
        if ball.y - ball.radius <= 0:
            self.sound.play()
            ball.y_vel *= -1
        if ball.y + ball.radius >= self.HEIGHT:
            self.sound.play()
            ball.y_vel *= -1

        if ball.x + ball.radius >= right_paddle.x:
            if right_paddle.y + right_paddle.height >= ball.y >= right_paddle.y:
                self.sound.play()
                ball.x_vel *= -1

                middle_paddle = right_paddle.y + right_paddle.height / 2
                difference = (middle_paddle - ball.y) / middle_paddle
                ball.y_vel = - difference * ball.VEL

        if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
            if left_paddle.y + left_paddle.height >= ball.y >= left_paddle.y:
                self.sound.play()
                ball.x_vel *= -1
                # ball.y_vel = random.randint(-ball.VEL, ball.VEL) for fun
                middle_paddle = left_paddle.y + left_paddle.height / 2
                difference = (middle_paddle - ball.y) / middle_paddle
                ball.y_vel = - difference * ball.VEL

    def draw(self, win, left_paddle, right_paddle, ball, left_score, right_score):
        win.fill(self.BLACK)
        left_paddle.draw(win)
        right_paddle.draw(win)

        ball.draw(win)
        pygame.draw.line(win, self.WHITE, (self.WIDTH // 2, 0), (self.WIDTH // 2, self.HEIGHT))

        text_left = self.font.render(str(left_score), True, self.WHITE)
        text_right = self.font.render(str(right_score), True, self.WHITE)
        win.blit(text_left, (self.WIDTH // 4, 20))
        win.blit(text_right, (3 * self.WIDTH // 4, 20))

        pygame.display.update()

    def movement(self, keys, left_paddle, right_paddle):
        if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height + right_paddle.VEL <= self.HEIGHT:
            right_paddle.move()

        if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.y + left_paddle.height + left_paddle.VEL <= self.HEIGHT:
            left_paddle.move()

    def check_points(self, ball):
        if ball.x < 0:
            self.right_score += 1
            ball.reset()
        elif ball.x > self.WIDTH:
            self.left_score += 1
            ball.reset()

    def win(self, screen):
        won = False
        win_text = ''
        if self.left_score >= self.WIN_SCORE:
            won = True
            win_text = "Left Player won!"
        if self.right_score >= self.WIN_SCORE:
            won = True
            win_text = "Right Player won!"

        if won:
            text = self.font.render(win_text, True, self.WHITE)
            screen.blit(text, ((self.WIDTH // 2) - text.get_width() // 2, self.HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(800)
            return True
        return False

    def game_loop(self, screen):

        clock = pygame.time.Clock()
        left_paddle = Paddles(10, self.HEIGHT // 2 - self.PADDLE_HEIGHT // 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        right_paddle = Paddles(self.WIDTH - 10 - self.PADDLE_WIDTH, self.HEIGHT // 2 - self.PADDLE_HEIGHT // 2,
                               self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, self.RADIUS)

        while True:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            keys = pygame.key.get_pressed()
            self.movement(keys, left_paddle, right_paddle)

            ball.move()
            self.collisions(left_paddle, right_paddle, ball)
            self.check_points(ball)

            self.draw(screen, left_paddle, right_paddle, ball, self.left_score, self.right_score)

            if self.win(screen):
                return False
