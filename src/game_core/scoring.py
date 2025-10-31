"""
Score calculation and tracking
"""
from .constants import *

class ScoreManager:
    """Manages game scoring system."""
    
    def __init__(self):
        """Initialize score manager."""
        self.current_score: int = 0
        self.high_score: int = 0
        self.food_eaten: int = 0
    
    def add_food_score(self) -> int:
        """Add score for eating food. Returns new score."""
        self.current_score += FOOD_SCORE
        self.food_eaten += 1
        
        # Update high score if current exceeds it
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        
        return self.current_score
    
    def get_current_score(self) -> int:
        """Get current game score."""
        return self.current_score
    
    def get_high_score(self) -> int:
        """Get high score."""
        return self.high_score
    
    def get_food_eaten(self) -> int:
        """Get number of food items eaten."""
        return self.food_eaten
    
    def reset_current_game(self) -> None:
        """Reset current game score but keep high score."""
        self.current_score = 0
        self.food_eaten = 0
    
    def reset_all(self) -> None:
        """Reset all scores including high score."""
        self.current_score = 0
        self.high_score = 0
        self.food_eaten = 0
    
    def get_score_info(self) -> dict:
        """Get comprehensive score information."""
        return {
            'current': self.current_score,
            'high': self.high_score,
            'food_eaten': self.food_eaten
        }