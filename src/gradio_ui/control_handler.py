"""
Control handler for Gradio interface
"""
from typing import Tuple, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core import GameEngine, UP, DOWN, LEFT, RIGHT

class ControlHandler:
    """Handles control actions from Gradio interface."""
    
    def __init__(self, game_engine: GameEngine):
        """Initialize control handler with game engine."""
        self.game_engine = game_engine
        self.last_action = "None"
        self.action_count = 0
    
    def move_up(self) -> Tuple[str, bool]:
        """Handle up movement."""
        if not self.game_engine.is_playing():
            return self._get_status_message(), False
        
        success = self.game_engine.handle_input(UP)
        if success:
            update_info = self.game_engine.update()
            self.last_action = "Move Up"
            self.action_count += 1
            return self._get_status_message(update_info), True
        else:
            return self._get_status_message(), False
    
    def move_down(self) -> Tuple[str, bool]:
        """Handle down movement."""
        if not self.game_engine.is_playing():
            return self._get_status_message(), False
        
        success = self.game_engine.handle_input(DOWN)
        if success:
            update_info = self.game_engine.update()
            self.last_action = "Move Down"
            self.action_count += 1
            return self._get_status_message(update_info), True
        else:
            return self._get_status_message(), False
    
    def move_left(self) -> Tuple[str, bool]:
        """Handle left movement."""
        if not self.game_engine.is_playing():
            return self._get_status_message(), False
        
        success = self.game_engine.handle_input(LEFT)
        if success:
            update_info = self.game_engine.update()
            self.last_action = "Move Left"
            self.action_count += 1
            return self._get_status_message(update_info), True
        else:
            return self._get_status_message(), False
    
    def move_right(self) -> Tuple[str, bool]:
        """Handle right movement."""
        if not self.game_engine.is_playing():
            return self._get_status_message(), False
        
        success = self.game_engine.handle_input(RIGHT)
        if success:
            update_info = self.game_engine.update()
            self.last_action = "Move Right"
            self.action_count += 1
            return self._get_status_message(update_info), True
        else:
            return self._get_status_message(), False
    
    def start_game(self) -> str:
        """Start a new game."""
        self.game_engine.start_game()
        self.last_action = "Start Game"
        self.action_count = 0
        return self._get_status_message()
    
    def pause_game(self) -> str:
        """Pause/Resume game."""
        if self.game_engine.is_playing():
            self.game_engine.pause_game()
            self.last_action = "Pause Game"
        elif self.game_engine.is_paused():
            self.game_engine.resume_game()
            self.last_action = "Resume Game"
        else:
            self.last_action = "Cannot Pause/Resume"
        
        return self._get_status_message()
    
    def reset_game(self) -> str:
        """Reset game to initial state."""
        self.game_engine.reset_game()
        self.last_action = "Reset Game"
        self.action_count = 0
        return self._get_status_message()
    
    def _get_status_message(self, update_info: Optional[dict] = None) -> str:
        """Generate status message for display."""
        game_state = self.game_engine.get_game_state()
        
        if not game_state.get('valid', False):
            return "❌ Game Error: Invalid state"
        
        score_info = game_state['score_info']
        snake_length = len(game_state['snake_body'])
        
        # Base status
        if game_state['game_over']:
            status = f"🔴 GAME OVER - Final Score: {score_info['current']}"
            if score_info['current'] == score_info['high'] and score_info['current'] > 0:
                status += " 🎉 NEW HIGH SCORE!"
        elif game_state['paused']:
            status = f"⏸️ PAUSED - Score: {score_info['current']}"
        else:
            status = f"🟢 PLAYING - Score: {score_info['current']}"
        
        # Add details
        status += f" | Length: {snake_length} | High: {score_info['high']}"
        
        # Add action feedback
        if update_info:
            if update_info['food_eaten']:
                status += " | 🍎 Food eaten!"
            if update_info['collision']:
                status += " | 💥 Collision!"
        
        # Add last action
        if self.last_action != "None":
            status += f" | Last: {self.last_action}"
        
        return status
    
    def get_game_info(self) -> dict:
        """Get comprehensive game information."""
        game_state = self.game_engine.get_game_state()
        
        return {
            'game_state': game_state,
            'last_action': self.last_action,
            'action_count': self.action_count,
            'is_playing': self.game_engine.is_playing(),
            'is_paused': self.game_engine.is_paused(),
            'is_game_over': self.game_engine.is_game_over()
        }