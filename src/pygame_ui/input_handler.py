"""
Pygame input handler for WASD controls
"""
import pygame
from typing import Optional, Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core import UP, DOWN, LEFT, RIGHT

class InputHandler:
    """Handles keyboard input for Pygame interface."""
    
    def __init__(self):
        """Initialize input handler."""
        self.key_map = {
            # WASD controls (primary)
            pygame.K_w: UP,
            pygame.K_a: LEFT,
            pygame.K_s: DOWN,
            pygame.K_d: RIGHT,
            
            # Arrow keys (secondary)
            pygame.K_UP: UP,
            pygame.K_LEFT: LEFT,
            pygame.K_DOWN: DOWN,
            pygame.K_RIGHT: RIGHT
        }
        
        self.quit_requested = False
        self.restart_requested = False
        self.pause_requested = False
    
    def handle_events(self) -> Optional[Tuple[int, int]]:
        """
        Process pygame events and return direction if movement key pressed.
        Returns None if no movement key pressed.
        """
        direction = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_requested = True
            
            elif event.type == pygame.KEYDOWN:
                # Handle movement keys
                if event.key in self.key_map:
                    direction = self.key_map[event.key]
                
                # Handle special keys
                elif event.key == pygame.K_r:
                    self.restart_requested = True
                elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    self.pause_requested = True
                elif event.key == pygame.K_ESCAPE:
                    self.quit_requested = True
        
        return direction
    
    def is_quit_requested(self) -> bool:
        """Check if quit was requested."""
        return self.quit_requested
    
    def is_restart_requested(self) -> bool:
        """Check if restart was requested and reset flag."""
        if self.restart_requested:
            self.restart_requested = False
            return True
        return False
    
    def is_pause_requested(self) -> bool:
        """Check if pause was requested and reset flag."""
        if self.pause_requested:
            self.pause_requested = False
            return True
        return False
    
    def reset_flags(self) -> None:
        """Reset all input flags."""
        self.quit_requested = False
        self.restart_requested = False
        self.pause_requested = False