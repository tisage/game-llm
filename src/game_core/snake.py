"""
Snake entity and behavior management
"""
from typing import List, Tuple, Optional
from .constants import *

class Snake:
    """Represents the Snake entity in the game."""
    
    def __init__(self, start_x: int, start_y: int):
        """Initialize snake at starting position."""
        self.body: List[Tuple[int, int]] = []
        self.direction: Tuple[int, int] = RIGHT
        self.grow_pending: bool = False
        
        # Initialize snake body with initial length
        for i in range(INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))
    
    def get_head_position(self) -> Tuple[int, int]:
        """Get the current head position."""
        return self.body[0]
    
    def get_body(self) -> List[Tuple[int, int]]:
        """Get the complete snake body."""
        return self.body.copy()
    
    def get_direction(self) -> Tuple[int, int]:
        """Get current movement direction."""
        return self.direction
    
    def change_direction(self, new_direction: Tuple[int, int]) -> bool:
        """
        Change snake direction if valid.
        Returns True if direction was changed, False if invalid.
        """
        # Prevent snake from going back into itself
        opposite_direction = (-self.direction[0], -self.direction[1])
        
        if new_direction != opposite_direction and new_direction in [UP, DOWN, LEFT, RIGHT]:
            self.direction = new_direction
            return True
        return False
    
    def move(self) -> None:
        """Move the snake one step in current direction."""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail unless growing
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def grow(self) -> None:
        """Mark snake to grow on next move."""
        self.grow_pending = True
    
    def check_self_collision(self) -> bool:
        """Check if snake head collides with its body."""
        head = self.body[0]
        return head in self.body[1:]
    
    def check_wall_collision(self, grid_width: int, grid_height: int) -> bool:
        """Check if snake head is outside grid boundaries."""
        head_x, head_y = self.body[0]
        return (head_x < 0 or head_x >= grid_width or 
                head_y < 0 or head_y >= grid_height)
    
    def get_length(self) -> int:
        """Get current snake length."""
        return len(self.body)
    
    def reset(self, start_x: int, start_y: int) -> None:
        """Reset snake to initial state."""
        self.body.clear()
        self.direction = RIGHT
        self.grow_pending = False
        
        # Reinitialize body
        for i in range(INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))