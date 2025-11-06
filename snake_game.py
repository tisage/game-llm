import pygame
import sys
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# --- Retro UI ---
STATUS_BAR_HEIGHT = 60
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = (SCREEN_HEIGHT - STATUS_BAR_HEIGHT) // GRID_SIZE
PLAY_AREA_Y_OFFSET = STATUS_BAR_HEIGHT
FONT_NAME = 'PressStart2P-Regular.ttf'

# Retro Color Palette (NES-like)
COLOR_BACKGROUND = (12, 12, 12)
COLOR_GRID_BG = (20, 20, 20)
COLOR_SNAKE_HEAD = (118, 204, 9)
COLOR_SNAKE_BODY = (80, 140, 20)
COLOR_SNAKE_OUTLINE = (12, 12, 12)
COLOR_FOOD = (214, 60, 60)
COLOR_FOOD_OUTLINE = (12, 12, 12)
COLOR_UI_TEXT = (230, 230, 230)
COLOR_UI_BORDER = (60, 60, 60)
COLOR_GAMEOVER = (214, 60, 60)

# Game settings
SNAKE_INITIAL_LENGTH = 3
SNAKE_SPEED_FPS = 10

class SnakeGame:
    """
    A class to encapsulate the Snake game logic and data with a retro UI style.
    """
    def __init__(self):
        """
        Initializes the game, sets up the screen, and resets the game state.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game - Retro Edition')
        self.clock = pygame.time.Clock()
        try:
            self.ui_font = pygame.font.Font(FONT_NAME, 16)
            self.message_font = pygame.font.Font(FONT_NAME, 40)
        except FileNotFoundError:
            print(f"Error: Font file '{FONT_NAME}' not found. Please place it in the root directory.")
            print("Using default font.")
            self.ui_font = pygame.font.Font(None, 24)
            self.message_font = pygame.font.Font(None, 50)

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
        
        # Center the snake in the new playable area
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = [(start_x, start_y)]
        for i in range(1, SNAKE_INITIAL_LENGTH):
            self.snake.append((start_x - i, start_y))
        
        self.direction = 'RIGHT'
        self.new_direction = 'RIGHT'
        
        self.food = []
        self._spawn_food(3)

    def _spawn_food(self, count=1):
        """
        Spawns food, ensuring it's not in the status bar area or on the snake.
        """
        for _ in range(count):
            while True:
                # Position is relative to the playable grid
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
        Updates snake position and checks for collisions within the playable area.
        """
        self.direction = self.new_direction
        head_x, head_y = self.snake[0]

        if self.direction == 'UP': head_y -= 1
        elif self.direction == 'DOWN': head_y += 1
        elif self.direction == 'LEFT': head_x -= 1
        elif self.direction == 'RIGHT': head_x += 1

        new_head = (head_x, head_y)

        # Check for wall collision (within the playable grid)
        if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
            self.game_over = True
            return

        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head in self.food:
            self.score += 10
            self.food.remove(new_head)
            self._spawn_food()
        else:
            self.snake.pop()

    def _draw_pixel_block(self, grid_pos, color, outline_color):
        """ Helper to draw a block with an outline in the playable grid. """
        x = grid_pos[0] * GRID_SIZE
        y = grid_pos[1] * GRID_SIZE + PLAY_AREA_Y_OFFSET
        
        # Draw outline
        pygame.draw.rect(self.screen, outline_color, (x, y, GRID_SIZE, GRID_SIZE))
        # Draw inner fill
        pygame.draw.rect(self.screen, color, (x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2))

    def _draw_elements(self):
        """
        Renders all game elements with a retro style.
        """
        self.screen.fill(COLOR_BACKGROUND)
        
        # --- Draw UI / Status Bar ---
        pygame.draw.rect(self.screen, COLOR_UI_BORDER, (0, 0, SCREEN_WIDTH, STATUS_BAR_HEIGHT))
        pygame.draw.rect(self.screen, COLOR_BACKGROUND, (2, 2, SCREEN_WIDTH - 4, STATUS_BAR_HEIGHT - 4))
        
        score_text = self.ui_font.render(f"SCORE: {self.score}", True, COLOR_UI_TEXT)
        self.screen.blit(score_text, (20, 20))
        
        food_text = self.ui_font.render(f"FOOD: {len(self.food)}", True, COLOR_UI_TEXT)
        food_rect = food_text.get_rect(right=SCREEN_WIDTH - 20, top=20)
        self.screen.blit(food_text, food_rect)

        # --- Draw Play Area ---
        play_area_rect = (0, PLAY_AREA_Y_OFFSET, SCREEN_WIDTH, SCREEN_HEIGHT - PLAY_AREA_Y_OFFSET)
        pygame.draw.rect(self.screen, COLOR_GRID_BG, play_area_rect)
        pygame.draw.rect(self.screen, COLOR_UI_BORDER, play_area_rect, 2)

        # Draw snake
        for i, segment in enumerate(self.snake):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            self._draw_pixel_block(segment, color, COLOR_SNAKE_OUTLINE)

        # Draw food
        for item in self.food:
            self._draw_pixel_block(item, COLOR_FOOD, COLOR_FOOD_OUTLINE)

        if self.game_over:
            self._draw_game_over()
        elif self.paused:
            self._draw_paused_message()

        pygame.display.flip()

    def _draw_message(self, text, font, color, y_offset=0):
        """ Helper to draw centered messages. """
        message_surf = font.render(text, True, color)
        message_rect = message_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + y_offset))
        self.screen.blit(message_surf, message_rect)

    def _draw_paused_message(self):
        """ Displays the 'PAUSED' message. """
        self._draw_message("PAUSED", self.message_font, COLOR_UI_TEXT)

    def _draw_game_over(self):
        """ Displays the 'GAME OVER' message. """
        self._draw_message("GAME OVER", self.message_font, COLOR_GAMEOVER, y_offset=-30)
        self._draw_message("Press 'R' to Restart", self.ui_font, COLOR_UI_TEXT, y_offset=30)


if __name__ == '__main__':
    game = SnakeGame()
    game.run()
