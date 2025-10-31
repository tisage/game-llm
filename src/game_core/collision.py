"""
Collision detection logic
"""
from typing import List, Tuple
from .constants import *

class CollisionDetector:
    """Handles all collision detection logic."""
    
    @staticmethod
    def check_wall_collision(position: Tuple[int, int], 
                           grid_width: int = GRID_WIDTH, 
                           grid_height: int = GRID_HEIGHT) -> bool:
        """Check if position is outside grid boundaries."""
        x, y = position
        return x < 0 or x >= grid_width or y < 0 or y >= grid_height
    
    @staticmethod
    def check_self_collision(head: Tuple[int, int], 
                           body: List[Tuple[int, int]]) -> bool:
        """Check if head collides with snake body (excluding head itself)."""
        return head in body[1:]  # Skip head (index 0)
    
    @staticmethod
    def check_food_collision(snake_head: Tuple[int, int], 
                           food_position: Tuple[int, int]) -> bool:
        """Check if snake head collides with food."""
        return snake_head == food_position
    
    @staticmethod
    def check_any_collision(snake_head: Tuple[int, int],
                          snake_body: List[Tuple[int, int]],
                          grid_width: int = GRID_WIDTH,
                          grid_height: int = GRID_HEIGHT) -> bool:
        """Check if snake head collides with walls or itself."""
        return (CollisionDetector.check_wall_collision(snake_head, grid_width, grid_height) or
                CollisionDetector.check_self_collision(snake_head, snake_body))