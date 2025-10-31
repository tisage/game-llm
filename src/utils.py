"""
🛠️ Utility Functions for Snake Game
AI-Powered Game Development Workshop

Helper functions and utilities for the Snake game project.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List
import random

def create_enhanced_grid_image(
    rgb_grid: np.ndarray, 
    cell_size: int = 30,
    border_width: int = 1,
    border_color: Tuple[int, int, int] = (100, 100, 100)
) -> Image.Image:
    """
    Create enhanced grid image with borders and better visuals
    
    Args:
        rgb_grid: RGB array from game state
        cell_size: Size of each cell in pixels
        border_width: Width of grid borders
        border_color: Color of grid borders
        
    Returns:
        PIL Image with enhanced visuals
    """
    grid_h, grid_w = rgb_grid.shape[:2]
    
    # Calculate total image size including borders
    img_width = grid_w * cell_size + (grid_w + 1) * border_width
    img_height = grid_h * cell_size + (grid_h + 1) * border_width
    
    # Create image with border color background
    image = Image.new('RGB', (img_width, img_height), border_color)
    
    # Fill in cells
    for i in range(grid_h):
        for j in range(grid_w):
            # Calculate cell position
            x = j * (cell_size + border_width) + border_width
            y = i * (cell_size + border_width) + border_width
            
            # Get cell color
            cell_color = tuple(rgb_grid[i, j])
            
            # Create cell rectangle
            cell_img = Image.new('RGB', (cell_size, cell_size), cell_color)
            image.paste(cell_img, (x, y))
    
    return image

def add_game_overlay(
    image: Image.Image,
    score: int,
    game_state: str,
    snake_length: int
) -> Image.Image:
    """
    Add text overlay with game information
    
    Args:
        image: Base game image
        score: Current score
        game_state: Current game state
        snake_length: Current snake length
        
    Returns:
        Image with overlay text
    """
    # Create a copy to avoid modifying original
    overlay_img = image.copy()
    draw = ImageDraw.Draw(overlay_img)
    
    # Try to use a decent font, fall back to default
    try:
        font = ImageFont.truetype("Arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    # Add text information
    text_lines = [
        f"Score: {score}",
        f"Length: {snake_length}",
        f"State: {game_state}"
    ]
    
    # Draw text with background
    y_offset = 10
    for line in text_lines:
        # Get text size
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Draw background rectangle
        draw.rectangle([5, y_offset, text_width + 15, y_offset + text_height + 5], 
                      fill=(0, 0, 0, 128))
        
        # Draw text
        draw.text((10, y_offset), line, fill=(255, 255, 255), font=font)
        y_offset += text_height + 8
    
    return overlay_img

def generate_random_food_colors() -> List[Tuple[int, int, int]]:
    """
    Generate random colors for food items
    
    Returns:
        List of RGB color tuples
    """
    colors = [
        (255, 0, 0),    # Red
        (255, 165, 0),  # Orange
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (255, 192, 203) # Pink
    ]
    return colors

def calculate_game_stats(snake_positions: List[Tuple[int, int]], 
                        grid_size: int) -> dict:
    """
    Calculate various game statistics
    
    Args:
        snake_positions: List of snake segment positions
        grid_size: Size of the game grid
        
    Returns:
        Dictionary with game statistics
    """
    if not snake_positions:
        return {
            'coverage_percent': 0,
            'efficiency_score': 0,
            'snake_density': 0
        }
    
    total_cells = grid_size * grid_size
    snake_length = len(snake_positions)
    
    # Calculate coverage percentage
    coverage_percent = (snake_length / total_cells) * 100
    
    # Calculate efficiency (how well snake fills the space)
    head_x, head_y = snake_positions[0]
    center_x, center_y = grid_size // 2, grid_size // 2
    distance_from_center = abs(head_x - center_x) + abs(head_y - center_y)
    max_distance = grid_size
    
    efficiency_score = max(0, 100 - (distance_from_center / max_distance) * 100)
    
    # Calculate snake density (how compact the snake is)
    if snake_length > 1:
        min_x = min(pos[0] for pos in snake_positions)
        max_x = max(pos[0] for pos in snake_positions)
        min_y = min(pos[1] for pos in snake_positions)
        max_y = max(pos[1] for pos in snake_positions)
        
        bounding_area = (max_x - min_x + 1) * (max_y - min_y + 1)
        snake_density = (snake_length / bounding_area) * 100 if bounding_area > 0 else 0
    else:
        snake_density = 100
    
    return {
        'coverage_percent': round(coverage_percent, 1),
        'efficiency_score': round(efficiency_score, 1),
        'snake_density': round(snake_density, 1)
    }

def create_demo_scenarios() -> List[dict]:
    """
    Create pre-configured scenarios for workshop demonstration
    
    Returns:
        List of scenario configurations
    """
    scenarios = [
        {
            'name': 'Beginner Demo',
            'grid_size': 8,
            'initial_length': 3,
            'description': 'Small grid for easy following'
        },
        {
            'name': 'Standard Game',
            'grid_size': 10,
            'initial_length': 3,
            'description': 'Classic Snake game setup'
        },
        {
            'name': 'Challenge Mode',
            'grid_size': 15,
            'initial_length': 5,
            'description': 'Larger grid with longer starting snake'
        },
        {
            'name': 'Workshop Demo',
            'grid_size': 6,
            'initial_length': 2,
            'description': 'Perfect for live coding demonstration'
        }
    ]
    
    return scenarios

def validate_game_state(snake_positions: List[Tuple[int, int]], 
                       food_position: Tuple[int, int],
                       grid_size: int) -> List[str]:
    """
    Validate current game state and return any issues found
    
    Args:
        snake_positions: Current snake positions
        food_position: Current food position
        grid_size: Game grid size
        
    Returns:
        List of validation error messages
    """
    errors = []
    
    # Check snake positions
    if not snake_positions:
        errors.append("Snake has no positions")
        return errors
    
    # Check positions are within bounds
    for i, (x, y) in enumerate(snake_positions):
        if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
            errors.append(f"Snake segment {i} is out of bounds: ({x}, {y})")
    
    # Check for duplicate positions in snake
    if len(snake_positions) != len(set(snake_positions)):
        errors.append("Snake has overlapping segments")
    
    # Check food position
    fx, fy = food_position
    if fx < 0 or fx >= grid_size or fy < 0 or fy >= grid_size:
        errors.append(f"Food is out of bounds: ({fx}, {fy})")
    
    # Check food not on snake
    if food_position in snake_positions:
        errors.append("Food is placed on snake")
    
    return errors

# AI-generated color palettes for workshop demonstration
def get_ai_color_palette(theme: str = "classic") -> dict:
    """
    Get AI-suggested color palettes for different themes
    
    Args:
        theme: Color theme name
        
    Returns:
        Dictionary with color mappings
    """
    palettes = {
        "classic": {
            'empty': (40, 40, 40),
            'snake_body': (0, 255, 0),
            'snake_head': (0, 180, 0),
            'food': (255, 50, 50)
        },
        "ocean": {
            'empty': (20, 50, 80),
            'snake_body': (0, 200, 255),
            'snake_head': (0, 150, 255),
            'food': (255, 200, 0)
        },
        "forest": {
            'empty': (34, 49, 34),
            'snake_body': (124, 252, 0),
            'snake_head': (85, 170, 85),
            'food': (255, 69, 0)
        },
        "neon": {
            'empty': (10, 10, 10),
            'snake_body': (57, 255, 20),
            'snake_head': (255, 20, 147),
            'food': (255, 215, 0)
        }
    }
    
    return palettes.get(theme, palettes["classic"])

# Testing utilities
def run_performance_test(grid_size: int = 20, steps: int = 1000) -> dict:
    """
    Run performance test for game logic
    
    Args:
        grid_size: Size of test grid
        steps: Number of steps to simulate
        
    Returns:
        Performance metrics
    """
    import time
    from snake_game import SnakeGame, Direction
    
    game = SnakeGame(grid_size)
    directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
    
    start_time = time.time()
    
    for _ in range(steps):
        # Random direction
        direction = random.choice(directions)
        if not game.step(direction):
            game.reset()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return {
        'total_time': round(execution_time, 3),
        'steps_per_second': round(steps / execution_time, 1),
        'grid_size': grid_size,
        'total_steps': steps
    }

if __name__ == "__main__":
    # Test utilities
    print("🧪 Testing Snake Game Utilities...")
    
    # Test performance
    perf_results = run_performance_test(10, 100)
    print(f"Performance test: {perf_results}")
    
    # Test color palettes
    themes = ["classic", "ocean", "forest", "neon"]
    for theme in themes:
        palette = get_ai_color_palette(theme)
        print(f"{theme.capitalize()} palette: {palette}")
    
    print("✅ Utilities test completed!")