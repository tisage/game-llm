"""
Main Pygame game loop
"""
import pygame
import sys
import os
from typing import Optional

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core import GameEngine, GameState
from game_core.constants import *
from .renderer import PygameRenderer
from .input_handler import InputHandler

class PygameGameLoop:
    """Main Pygame game loop managing the game."""
    
    def __init__(self):
        """Initialize Pygame game loop."""
        # Initialize Pygame
        pygame.init()
        
        # Create screen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("🐍 Snake Game - Click here and use WASD!")
        
        # Set window icon if possible
        try:
            # Create a simple snake icon
            icon = pygame.Surface((32, 32))
            icon.fill(GREEN)
            pygame.display.set_icon(icon)
        except:
            pass
        
        # Game components
        self.clock = pygame.time.Clock()
        self.game_engine = GameEngine()
        self.renderer = PygameRenderer(self.screen)
        self.input_handler = InputHandler()
        
        # Game state
        self.running = True
        self.last_move_time = 0
        
        print("🎮 Pygame Snake Game Initialized!")
        print("=" * 50)
        print("IMPORTANT: Click on the game window to focus it!")
        print("=" * 50)
        print("Controls:")
        print("  WASD or Arrow Keys - Move snake")
        print("  R - Restart game")
        print("  P/Space - Pause/Resume")
        print("  ESC - Quit game")
        print("=" * 50)
    
    def run(self) -> None:
        """Main game loop."""
        self.game_engine.start_game()
        
        print("🎮 Game started! Make sure the Pygame window has focus and try WASD keys.")
        
        while self.running:
            current_time = pygame.time.get_ticks()
            
            # Handle input first (immediately responsive)
            self._handle_input()
            
            # Only update game logic automatically if no input was just processed
            if current_time - self.last_move_time >= INITIAL_SNAKE_SPEED:
                if self.game_engine.is_playing():
                    update_info = self.game_engine.update()
                    self._handle_update_info(update_info)
                self.last_move_time = current_time
            
            # Render frame
            self._render()
            
            # Control frame rate (60 FPS for smooth rendering)
            self.clock.tick(60)
        
        self._cleanup()
    
    def _handle_input(self) -> None:
        """Handle all input events."""
        direction = self.input_handler.handle_events()
        
        # Handle quit
        if self.input_handler.is_quit_requested():
            self.running = False
            return
        
        # Handle restart
        if self.input_handler.is_restart_requested():
            self.game_engine.start_game()
            self.last_move_time = pygame.time.get_ticks()  # Reset timer
            return
        
        # Handle pause/resume
        if self.input_handler.is_pause_requested():
            if self.game_engine.is_playing():
                self.game_engine.pause_game()
            elif self.game_engine.is_paused():
                self.game_engine.resume_game()
            return
        
        # Handle movement - move immediately when key is pressed
        if direction and self.game_engine.is_playing():
            success = self.game_engine.handle_input(direction)
            if success:
                # Move immediately and reset timer
                update_info = self.game_engine.update()
                self._handle_update_info(update_info)
                self.last_move_time = pygame.time.get_ticks()
                # Print direction for debugging
                direction_names = {UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT"}
                print(f"🎯 Snake moved: {direction_names.get(direction, direction)}")
    
    def _handle_update_info(self, update_info: dict) -> None:
        """Handle game update information."""
        if update_info['game_ended']:
            print(f"Game Over! Final Score: {update_info['score']}")
        elif update_info['food_eaten']:
            print(f"Food eaten! Score: {update_info['score']}, Length: {update_info['snake_length']}")
    
    def _render(self) -> None:
        """Render current frame."""
        game_state = self.game_engine.get_game_state()
        self.renderer.render_frame(game_state)
        pygame.display.flip()
    
    def _cleanup(self) -> None:
        """Clean up resources."""
        pygame.quit()
        print("🐍 Game ended. Thanks for playing!")

def main():
    """Main entry point for Pygame version."""
    try:
        game = PygameGameLoop()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()