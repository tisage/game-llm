
import pygame
import sys

# --- Constants ---
# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle properties
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Ball properties
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Score
WINNING_SCORE = 11

class PongGame:
    """
    A class to represent the Pong game.
    """
    def __init__(self):
        """
        Initialize the game.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        """
        Reset the game to its initial state.
        """
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None
        self.reset_ball()

        self.left_paddle = pygame.Rect(30, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(SCREEN_WIDTH - 30 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    def reset_ball(self, direction=1):
        """
        Reset the ball to the center.
        """
        self.ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.ball_speed_x = BALL_SPEED_X * direction
        self.ball_speed_y = BALL_SPEED_Y

    def handle_input(self):
        """
        Handle user input.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.left_paddle.top > 0:
            self.left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and self.left_paddle.bottom < SCREEN_HEIGHT:
            self.left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and self.right_paddle.top > 0:
            self.right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and self.right_paddle.bottom < SCREEN_HEIGHT:
            self.right_paddle.y += PADDLE_SPEED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()

    def update(self):
        """
        Update game state.
        """
        if self.game_over:
            return

        # Move the ball
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Ball collision with top/bottom walls
        if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
            self.ball_speed_y *= -1

        # Ball collision with paddles
        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_speed_x *= -1

        # Ball goes out of bounds
        if self.ball.left <= 0:
            self.player2_score += 1
            if self.player2_score >= WINNING_SCORE:
                self.game_over = True
                self.winner = "Player 2"
            else:
                self.reset_ball(1) # Move towards player 1
        if self.ball.right >= SCREEN_WIDTH:
            self.player1_score += 1
            if self.player1_score >= WINNING_SCORE:
                self.game_over = True
                self.winner = "Player 1"
            else:
                self.reset_ball(-1) # Move towards player 2


    def render(self):
        """
        Render the game.
        """
        self.screen.fill(BLACK)

        # Draw paddles
        pygame.draw.rect(self.screen, WHITE, self.left_paddle)
        pygame.draw.rect(self.screen, WHITE, self.right_paddle)

        # Draw ball
        pygame.draw.ellipse(self.screen, WHITE, self.ball)

        # Draw net
        for i in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.line(self.screen, WHITE, (SCREEN_WIDTH // 2, i), (SCREEN_WIDTH // 2, i + 10), 1)

        # Draw score
        player1_text = self.small_font.render(str(self.player1_score), True, WHITE)
        self.screen.blit(player1_text, (SCREEN_WIDTH // 4, 20))

        player2_text = self.small_font.render(str(self.player2_score), True, WHITE)
        self.screen.blit(player2_text, (SCREEN_WIDTH * 3 // 4, 20))

        if self.game_over:
            win_text = self.font.render(f"{self.winner} Wins!", True, WHITE)
            win_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(win_text, win_rect)

            restart_text = self.small_font.render("Press 'R' to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(restart_text, restart_rect)


        pygame.display.flip()

    def run(self):
        """
        Main game loop.
        """
        while True:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    game = PongGame()
    game.run()
