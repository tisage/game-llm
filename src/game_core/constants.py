# Game Configuration Constants

# Grid dimensions
GRID_WIDTH = 20
GRID_HEIGHT = 15
CELL_SIZE = 30

# Window dimensions
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 100  # Extra space for UI

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

# Game settings
FPS = 10
INITIAL_SNAKE_LENGTH = 3
INITIAL_SNAKE_SPEED = 300  # milliseconds (slower automatic movement)

# Directions (x, y)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game states
class GameState:
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    RESET = "reset"

# Score settings
FOOD_SCORE = 10

# Food settings
MAX_FOOD_COUNT = 3  # Maximum number of food items on board
MIN_FOOD_COUNT = 2  # Minimum number of food items on board

# Food colors for variety
FOOD_COLORS = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange  
    (255, 255, 0),  # Yellow
    (255, 20, 147), # Deep Pink
    (138, 43, 226), # Blue Violet
]