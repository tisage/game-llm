"""
🐍 Snake Game - Core Game Logic
AI-Powered Game Development Workshop

This module contains the main game logic for the Snake game.
Created using GitHub Copilot CLI assistance.
"""

import numpy as np
from typing import List, Tuple, Optional
from enum import Enum
import random

class Direction(Enum):
    """Enumeration for snake movement directions"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class GameState(Enum):
    """Enumeration for game states"""
    PLAYING = "playing"
    GAME_OVER = "game_over"
    NOT_STARTED = "not_started"

class SnakeGame:
    """
    Main Snake Game class
    
    Handles all game logic including:
    - Snake movement and growth
    - Food placement and consumption
    - Collision detection
    - Score tracking
    - Visual representation
    """
    
    def __init__(self, grid_size: int = 10):
        """
        Initialize the Snake game
        
        Args:
            grid_size (int): Size of the game grid (default: 10x10)
        """
        self.grid_size = grid_size
        self.reset()
    
    def reset(self):
        """Reset the game to initial state"""
        # Initialize empty grid
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        
        # Place snake in center of grid
        center = self.grid_size // 2
        self.snake = [(center, center)]
        
        # Set initial direction
        self.direction = Direction.RIGHT
        
        # Place first food
        self.food = self._place_food()
        
        # Initialize game state
        self.score = 0
        self.state = GameState.NOT_STARTED
        
        # Update visual representation
        self._update_grid()
    
    def _place_food(self) -> Tuple[int, int]:
        """
        Place food randomly on empty cells
        
        Returns:
            Tuple[int, int]: Coordinates of placed food
        """
        # Find all empty cells (not occupied by snake)
        empty_cells = []
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if (x, y) not in self.snake:
                    empty_cells.append((x, y))
        
        # Return random empty cell, or (0,0) if no empty cells
        return random.choice(empty_cells) if empty_cells else (0, 0)
    
    def _update_grid(self):
        """Update the visual grid representation"""
        # Clear grid
        self.grid.fill(0)  # Empty cells = 0
        
        # Place snake on grid
        for i, (x, y) in enumerate(self.snake):
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.grid[y, x] = 2 if i == 0 else 1  # Head = 2, Body = 1
        
        # Place food on grid
        fx, fy = self.food
        if 0 <= fx < self.grid_size and 0 <= fy < self.grid_size:
            self.grid[fy, fx] = 3  # Food = 3
    
    def step(self, new_direction: Optional[Direction] = None) -> bool:
        """
        Execute one game step
        
        Args:
            new_direction (Optional[Direction]): New direction for snake movement
            
        Returns:
            bool: True if game continues, False if game over
        """
        if self.state == GameState.GAME_OVER:
            return False
        
        # Start game if not started
        self.state = GameState.PLAYING
        
        # Update direction if provided and valid
        if new_direction and self._is_valid_direction(new_direction):
            self.direction = new_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check for collisions
        if self._check_collision(new_head):
            self.state = GameState.GAME_OVER
            return False
        
        # Move snake (add new head)
        self.snake.insert(0, new_head)
        
        # Check if food was eaten
        if new_head == self.food:
            # Snake grows (don't remove tail)
            self.score += 1
            self.food = self._place_food()
        else:
            # Snake doesn't grow (remove tail)
            self.snake.pop()
        
        # Update visual representation
        self._update_grid()
        return True
    
    def _is_valid_direction(self, new_direction: Direction) -> bool:
        """
        Check if direction change is valid (prevents immediate reversal)
        
        Args:
            new_direction (Direction): Direction to validate
            
        Returns:
            bool: True if direction change is valid
        """
        # Allow any direction if snake is just head
        if len(self.snake) < 2:
            return True
        
        # Get current and new direction vectors
        current_dx, current_dy = self.direction.value
        new_dx, new_dy = new_direction.value
        
        # Prevent immediate reversal (180-degree turn)
        return not (current_dx == -new_dx and current_dy == -new_dy)
    
    def _check_collision(self, position: Tuple[int, int]) -> bool:
        """
        Check if position causes collision
        
        Args:
            position (Tuple[int, int]): Position to check
            
        Returns:
            bool: True if collision detected
        """
        x, y = position
        
        # Check wall collision
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return True
        
        # Check self collision
        if position in self.snake:
            return True
        
        return False
    
    def get_visual_grid(self) -> np.ndarray:
        """
        Get colored grid for visualization
        
        Returns:
            np.ndarray: RGB array representing the game state
        """
        # Create RGB image (height, width, 3 channels)
        rgb_grid = np.zeros((self.grid_size, self.grid_size, 3), dtype=np.uint8)
        
        # Define color mapping
        colors = {
            0: [40, 40, 40],     # Empty cells - dark gray
            1: [0, 255, 0],      # Snake body - bright green
            2: [0, 180, 0],      # Snake head - darker green
            3: [255, 50, 50],    # Food - bright red
        }
        
        # Apply colors to grid
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_value = self.grid[i, j]
                rgb_grid[i, j] = colors[cell_value]
        
        return rgb_grid
    
    def get_game_info(self) -> dict:
        """
        Get current game information
        
        Returns:
            dict: Game state information
        """
        return {
            'score': self.score,
            'snake_length': len(self.snake),
            'state': self.state.value,
            'food_position': self.food,
            'snake_head': self.snake[0] if self.snake else None,
            'direction': self.direction.name
        }

# Quick test function for development
def test_snake_game():
    """Test function to verify game functionality"""
    print("🐍 Testing Snake Game Logic...")
    
    # Create game instance
    game = SnakeGame(10)
    print(f"Initial state: {game.get_game_info()}")
    
    # Test movement
    for i in range(3):
        game.step()
        info = game.get_game_info()
        print(f"Step {i+1}: Score={info['score']}, Head at {info['snake_head']}")
    
    # Test direction change
    game.step(Direction.DOWN)
    print(f"After turning down: {game.get_game_info()}")
    
    print("✅ Snake game logic test completed!")

if __name__ == "__main__":
    test_snake_game()