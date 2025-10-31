"""
Food generation and management
"""
import random
from typing import List, Tuple
from .constants import *

class Food:
    """Represents food in the Snake game."""
    
    def __init__(self, grid_width: int = GRID_WIDTH, grid_height: int = GRID_HEIGHT):
        """Initialize food manager."""
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position: Tuple[int, int] = (0, 0)
        self._generate_new_position()
    
    def _generate_new_position(self) -> None:
        """Generate a random position for food."""
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        self.position = (x, y)
    
    def get_position(self) -> Tuple[int, int]:
        """Get current food position."""
        return self.position
    
    def respawn(self, snake_body: List[Tuple[int, int]]) -> None:
        """
        Generate new food position avoiding snake body.
        Ensures food doesn't spawn on snake.
        """
        max_attempts = self.grid_width * self.grid_height
        attempts = 0
        
        while attempts < max_attempts:
            self._generate_new_position()
            if self.position not in snake_body:
                break
            attempts += 1
        
        # Fallback: if grid is nearly full, find first available spot
        if attempts >= max_attempts:
            for y in range(self.grid_height):
                for x in range(self.grid_width):
                    if (x, y) not in snake_body:
                        self.position = (x, y)
                        return
    
    def is_eaten(self, snake_head: Tuple[int, int]) -> bool:
        """Check if food is eaten by snake head."""
        return self.position == snake_head
    
    def reset(self, snake_body: List[Tuple[int, int]]) -> None:
        """Reset food to new random position."""
        self.respawn(snake_body)