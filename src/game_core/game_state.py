"""
Main game state management
"""
from typing import Optional, Dict, Any, Tuple
from .constants import *
from .snake import Snake
from .food import Food
from .collision import CollisionDetector
from .scoring import ScoreManager

class GameEngine:
    """Core game engine managing all game state and logic."""
    
    def __init__(self):
        """Initialize game engine."""
        self.grid_width = GRID_WIDTH
        self.grid_height = GRID_HEIGHT
        
        # Game components
        self.snake: Optional[Snake] = None
        self.food: Optional[Food] = None
        self.score_manager = ScoreManager()
        self.collision_detector = CollisionDetector()
        
        # Game state
        self.current_state = GameState.MENU
        self.game_over = False
        self.paused = False
        
        # Initialize game
        self.reset_game()
    
    def reset_game(self) -> None:
        """Reset game to initial state."""
        # Calculate starting position (center of grid)
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        
        # Initialize game components
        self.snake = Snake(start_x, start_y)
        self.food = Food(self.grid_width, self.grid_height)
        self.food.respawn(self.snake.get_body())
        
        # Reset game state
        self.score_manager.reset_current_game()
        self.current_state = GameState.PLAYING
        self.game_over = False
        self.paused = False
    
    def start_game(self) -> None:
        """Start a new game."""
        self.reset_game()
        self.current_state = GameState.PLAYING
    
    def pause_game(self) -> None:
        """Pause the current game."""
        if self.current_state == GameState.PLAYING:
            self.paused = True
            self.current_state = GameState.PAUSED
    
    def resume_game(self) -> None:
        """Resume paused game."""
        if self.current_state == GameState.PAUSED:
            self.paused = False
            self.current_state = GameState.PLAYING
    
    def end_game(self) -> None:
        """End current game."""
        self.game_over = True
        self.current_state = GameState.GAME_OVER
    
    def handle_input(self, direction: Tuple[int, int]) -> bool:
        """
        Handle player input for snake direction.
        Returns True if input was valid and processed.
        """
        if self.current_state != GameState.PLAYING or self.game_over or not self.snake:
            return False
        
        return self.snake.change_direction(direction)
    
    def update(self) -> Dict[str, Any]:
        """
        Update game state for one frame.
        Returns dict with update information.
        """
        if (self.current_state != GameState.PLAYING or 
            self.game_over or self.paused or not self.snake or not self.food):
            return self._get_update_info(False, False, False)
        
        # Move snake
        self.snake.move()
        
        # Check collisions
        snake_head = self.snake.get_head_position()
        snake_body = self.snake.get_body()
        
        # Check wall and self collision
        if self.collision_detector.check_any_collision(
            snake_head, snake_body, self.grid_width, self.grid_height):
            self.end_game()
            return self._get_update_info(True, False, True)
        
        # Check food collision with multiple food items
        food_eaten = False
        if hasattr(self.food, 'manager'):
            # New multiple food system
            eaten_food = self.food.manager.check_collision(snake_head)
            if eaten_food:
                self.snake.grow()
                self.score_manager.add_food_score()
                self.food.manager.remove_food(eaten_food)
                self.food.manager.update(snake_body)  # Spawn new food if needed
                food_eaten = True
        else:
            # Legacy single food system
            if self.collision_detector.check_food_collision(snake_head, self.food.get_position()):
                self.snake.grow()
                self.score_manager.add_food_score()
                self.food.respawn(snake_body)
                food_eaten = True
        
        return self._get_update_info(False, food_eaten, False)
    
    def _get_update_info(self, collision: bool, food_eaten: bool, game_ended: bool) -> Dict[str, Any]:
        """Get comprehensive update information."""
        return {
            'collision': collision,
            'food_eaten': food_eaten,
            'game_ended': game_ended,
            'score': self.score_manager.get_current_score(),
            'snake_length': self.snake.get_length() if self.snake else 0,
            'game_state': self.current_state
        }
    
    def get_game_state(self) -> Dict[str, Any]:
        """Get current complete game state."""
        if not self.snake or not self.food:
            return {
                'valid': False,
                'message': 'Game not initialized'
            }
        
        return {
            'valid': True,
            'snake_body': self.snake.get_body(),
            'snake_direction': self.snake.get_direction(),
            'food_position': self.food.get_position(),  # For compatibility
            'food_positions': getattr(self.food, 'manager', self.food).get_all_positions() if hasattr(self.food, 'manager') else [self.food.get_position()],
            'food_items': getattr(self.food, 'manager', self.food).get_all_food_items() if hasattr(self.food, 'manager') else [],
            'score_info': self.score_manager.get_score_info(),
            'game_over': self.game_over,
            'paused': self.paused,
            'current_state': self.current_state,
            'grid_size': (self.grid_width, self.grid_height)
        }
    
    def is_game_over(self) -> bool:
        """Check if game is over."""
        return self.game_over
    
    def is_paused(self) -> bool:
        """Check if game is paused."""
        return self.paused
    
    def is_playing(self) -> bool:
        """Check if game is actively playing."""
        return self.current_state == GameState.PLAYING and not self.game_over and not self.paused