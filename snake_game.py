import pygame
import sys
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (100, 255, 100)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Game settings
SNAKE_INITIAL_LENGTH = 3
SNAKE_SPEED_FPS = 10 # Frames per second, effectively controls speed

class SnakeGame:
    """
    A class to encapsulate the Snake game logic and data.
    """
    def __init__(self):
        """
        Initializes the game, sets up the screen, and resets the game state.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.paused = False
        self._reset_game_state()

    def _reset_game_state(self):
        """
        Resets the game to its initial state.
        """
        self.game_over = False
        self.paused = False
        self.score = 0
        
        # Initial snake position and direction
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        for i in range(1, SNAKE_INITIAL_LENGTH):
            self.snake.append((GRID_WIDTH // 2 - i, GRID_HEIGHT // 2))
        
        self.direction = 'RIGHT'
        self.new_direction = 'RIGHT'
        
        self.food = []
        self._spawn_food(3)

    def _spawn_food(self, count=1):
        """
        Spawns a specified number of food items at random locations.
        """
        for _ in range(count):
            while True:
                position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                if position not in self.snake and position not in self.food:
                    self.food.append(position)
                    break

    def run(self):
        """
        The main game loop.
        """
        while True:
            self._handle_input()
            if not self.game_over and not self.paused:
                self._update_game_state()
            self._draw_elements()
            self.clock.tick(SNAKE_SPEED_FPS)

    def _handle_input(self):
        """
        Handles user input for controlling the snake and game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and not self.game_over:
                    self.paused = not self.paused
                if self.game_over:
                    if event.key == pygame.K_r:
                        self._reset_game_state()
                elif not self.paused:
                    if event.key == pygame.K_w and self.direction != 'DOWN':
                        self.new_direction = 'UP'
                    elif event.key == pygame.K_s and self.direction != 'UP':
                        self.new_direction = 'DOWN'
                    elif event.key == pygame.K_a and self.direction != 'RIGHT':
                        self.new_direction = 'LEFT'
                    elif event.key == pygame.K_d and self.direction != 'LEFT':
                        self.new_direction = 'RIGHT'

    def _update_game_state(self):
        """
        Updates the position of the snake, checks for collisions, and handles food consumption.
        """
        self.direction = self.new_direction
        head_x, head_y = self.snake[0]

        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1

        new_head = (head_x, head_y)

        # Check for wall collision
        if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
            self.game_over = True
            return

        # Check for self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Check for food collision
        if new_head in self.food:
            self.score += 10
            self.food.remove(new_head)
            self._spawn_food()
        else:
            self.snake.pop()

    def _draw_elements(self):
        """
        Renders all game elements to the screen.
        """
        self.screen.fill(BLACK)
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = BRIGHT_GREEN if i == 0 else GREEN
            pygame.draw.rect(self.screen, color, rect)

        # Draw food
        for item in self.food:
            rect = pygame.Rect(item[0] * GRID_SIZE, item[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            # 3D-like effect for food
            pygame.draw.circle(self.screen, (150, 0, 0), rect.center, GRID_SIZE // 2) # Shadow
            pygame.draw.circle(self.screen, RED, (rect.centerx - 1, rect.centery - 1), GRID_SIZE // 2) # Main color
            pygame.draw.circle(self.screen, (255, 150, 150), (rect.centerx - 3, rect.centery - 3), GRID_SIZE // 4) # Highlight

        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        food_count_text = self.font.render(f"Food: {len(self.food)}", True, WHITE)
        self.screen.blit(food_count_text, (10, 40))

        if self.game_over:
            self._draw_game_over()
        elif self.paused:
            self._draw_paused_message()

        pygame.display.flip()

    def _draw_paused_message(self):
        """
        Displays the 'PAUSED' message.
        """
        paused_font = pygame.font.Font(None, 72)
        paused_text = paused_font.render("PAUSED", True, WHITE)
        paused_rect = paused_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(paused_text, paused_rect)

    def _draw_game_over(self):
        """
        Displays the 'GAME OVER' message.
        """
        over_font = pygame.font.Font(None, 72)
        over_text = over_font.render("GAME OVER", True, RED)
        over_rect = over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(over_text, over_rect)
        
        restart_font = pygame.font.Font(None, 36)
        restart_text = restart_font.render("Press 'R' to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        self.screen.blit(restart_text, restart_rect)


if __name__ == '__main__':
    game = SnakeGame()
    game.run()
