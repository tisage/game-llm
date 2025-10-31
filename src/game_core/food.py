"""
Food generation and management - Multiple food system
"""
import random
from typing import List, Tuple
from .constants import *

class FoodItem:
    """Represents a single food item."""
    
    def __init__(self, position: Tuple[int, int], color: Tuple[int, int, int] = None):
        """Initialize a food item."""
        self.position = position
        self.color = color or random.choice(FOOD_COLORS)
        self.value = FOOD_SCORE  # Can be modified for different food types
    
    def is_eaten_by(self, snake_head: Tuple[int, int]) -> bool:
        """Check if this food is eaten by snake head."""
        return self.position == snake_head

class FoodManager:
    """Manages multiple food items on the game board."""
    
    def __init__(self, grid_width: int = GRID_WIDTH, grid_height: int = GRID_HEIGHT):
        """Initialize food manager."""
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.food_items: List[FoodItem] = []
        self.target_food_count = MIN_FOOD_COUNT
    
    def _generate_position(self, avoid_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        """Generate a random position avoiding specified positions."""
        max_attempts = self.grid_width * self.grid_height
        attempts = 0
        
        while attempts < max_attempts:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            position = (x, y)
            
            if position not in avoid_positions:
                return position
            attempts += 1
        
        # Fallback: find first available spot
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if (x, y) not in avoid_positions:
                    return (x, y)
        
        # Ultimate fallback (shouldn't happen in normal gameplay)
        return (0, 0)
    
    def _get_all_occupied_positions(self, snake_body: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Get all positions occupied by snake and existing food."""
        occupied = snake_body.copy()
        occupied.extend([food.position for food in self.food_items])
        return occupied
    
    def spawn_food(self, snake_body: List[Tuple[int, int]]) -> None:
        """Spawn a new food item."""
        occupied_positions = self._get_all_occupied_positions(snake_body)
        new_position = self._generate_position(occupied_positions)
        new_color = random.choice(FOOD_COLORS)
        
        self.food_items.append(FoodItem(new_position, new_color))
    
    def update(self, snake_body: List[Tuple[int, int]]) -> None:
        """Update food items - maintain target count."""
        # Ensure we have the target number of food items
        while len(self.food_items) < self.target_food_count:
            self.spawn_food(snake_body)
    
    def check_collision(self, snake_head: Tuple[int, int]) -> FoodItem:
        """Check if snake head collides with any food. Returns eaten food or None."""
        for food in self.food_items:
            if food.is_eaten_by(snake_head):
                return food
        return None
    
    def remove_food(self, food_item: FoodItem) -> None:
        """Remove a specific food item."""
        if food_item in self.food_items:
            self.food_items.remove(food_item)
    
    def get_all_positions(self) -> List[Tuple[int, int]]:
        """Get positions of all food items."""
        return [food.position for food in self.food_items]
    
    def get_all_food_items(self) -> List[FoodItem]:
        """Get all food items."""
        return self.food_items.copy()
    
    def set_food_count(self, count: int) -> None:
        """Set target food count (between MIN and MAX)."""
        self.target_food_count = max(MIN_FOOD_COUNT, min(MAX_FOOD_COUNT, count))
    
    def reset(self, snake_body: List[Tuple[int, int]]) -> None:
        """Reset all food items."""
        self.food_items.clear()
        self.target_food_count = MIN_FOOD_COUNT
        self.update(snake_body)

# Legacy Food class for backward compatibility
class Food:
    """Legacy single food class - redirects to FoodManager."""
    
    def __init__(self, grid_width: int = GRID_WIDTH, grid_height: int = GRID_HEIGHT):
        """Initialize legacy food (uses FoodManager internally)."""
        self.manager = FoodManager(grid_width, grid_height)
        self.grid_width = grid_width
        self.grid_height = grid_height
    
    def get_position(self) -> Tuple[int, int]:
        """Get position of first food item (for compatibility)."""
        if self.manager.food_items:
            return self.manager.food_items[0].position
        return (0, 0)
    
    def respawn(self, snake_body: List[Tuple[int, int]]) -> None:
        """Respawn food (maintains multiple food items)."""
        self.manager.update(snake_body)
    
    def is_eaten(self, snake_head: Tuple[int, int]) -> bool:
        """Check if any food is eaten."""
        return self.manager.check_collision(snake_head) is not None
    
    def reset(self, snake_body: List[Tuple[int, int]]) -> None:
        """Reset food system."""
        self.manager.reset(snake_body)