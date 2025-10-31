"""
Game image renderer for Gradio interface
"""
import pygame
import numpy as np
from PIL import Image
from typing import Dict, Any, List, Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core.constants import *

class GameImageRenderer:
    """Renders game state to PIL Image for Gradio display."""
    
    def __init__(self):
        """Initialize the image renderer."""
        # Initialize pygame for surface operations (headless)
        pygame.init()
        
        # Create rendering surface
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Initialize fonts
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # UI areas
        self.game_area_height = GRID_HEIGHT * CELL_SIZE
        self.ui_area_y = self.game_area_height
    
    def render_game_state(self, game_state: Dict[str, Any]) -> Image.Image:
        """
        Render game state to PIL Image.
        Returns PIL Image that can be displayed in Gradio.
        """
        if not game_state.get('valid', False):
            return self._render_error(game_state.get('message', 'Invalid game state'))
        
        # Clear surface
        self.surface.fill(BLACK)
        
        # Draw game components
        self._draw_grid()
        self._draw_food(game_state['food_position'])
        self._draw_snake(game_state['snake_body'])
        self._draw_ui(game_state)
        
        # Draw overlays
        if game_state['game_over']:
            self._draw_game_over_overlay(game_state['score_info'])
        elif game_state['paused']:
            self._draw_paused_overlay()
        
        # Convert pygame surface to PIL Image
        return self._surface_to_pil_image()
    
    def _draw_grid(self) -> None:
        """Draw grid lines."""
        # Vertical lines
        for x in range(0, WINDOW_WIDTH + 1, CELL_SIZE):
            pygame.draw.line(self.surface, GRAY, 
                           (x, 0), (x, self.game_area_height))
        
        # Horizontal lines
        for y in range(0, self.game_area_height + 1, CELL_SIZE):
            pygame.draw.line(self.surface, GRAY, 
                           (0, y), (WINDOW_WIDTH, y))
    
    def _draw_snake(self, snake_body: List[Tuple[int, int]]) -> None:
        """Draw snake with enhanced visuals."""
        for i, (x, y) in enumerate(snake_body):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if i == 0:  # Head
                # Head with gradient effect
                pygame.draw.rect(self.surface, GREEN, rect)
                pygame.draw.rect(self.surface, WHITE, rect, 3)
                
                # Eyes
                eye_size = 6
                eye1_pos = (x * CELL_SIZE + 7, y * CELL_SIZE + 7)
                eye2_pos = (x * CELL_SIZE + CELL_SIZE - 13, y * CELL_SIZE + 7)
                
                pygame.draw.circle(self.surface, BLACK, eye1_pos, eye_size//2)
                pygame.draw.circle(self.surface, BLACK, eye2_pos, eye_size//2)
                pygame.draw.circle(self.surface, WHITE, eye1_pos, 1)
                pygame.draw.circle(self.surface, WHITE, eye2_pos, 1)
            else:  # Body
                # Body segments with slight gradient
                color_intensity = max(150, 255 - (i * 5))  # Fade towards tail
                body_color = (0, color_intensity, 0)
                pygame.draw.rect(self.surface, body_color, rect)
                pygame.draw.rect(self.surface, WHITE, rect, 1)
    
    def _draw_food(self, food_position: Tuple[int, int]) -> None:
        """Draw food with attractive visuals."""
        x, y = food_position
        center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
        radius = CELL_SIZE // 2 - 3
        
        # Food as apple-like circle
        pygame.draw.circle(self.surface, RED, center, radius)
        pygame.draw.circle(self.surface, (200, 0, 0), center, radius, 3)
        
        # Highlight
        highlight_pos = (center[0] - radius//3, center[1] - radius//3)
        pygame.draw.circle(self.surface, WHITE, highlight_pos, radius//4)
    
    def _draw_ui(self, game_state: Dict[str, Any]) -> None:
        """Draw comprehensive UI."""
        score_info = game_state['score_info']
        snake_length = len(game_state['snake_body'])
        
        # UI background
        ui_rect = pygame.Rect(0, self.ui_area_y, WINDOW_WIDTH, 100)
        pygame.draw.rect(self.surface, BLACK, ui_rect)
        pygame.draw.line(self.surface, WHITE, 
                        (0, self.ui_area_y), (WINDOW_WIDTH, self.ui_area_y), 2)
        
        # Score (large and prominent)
        score_text = self.font_large.render(f"Score: {score_info['current']}", True, WHITE)
        self.surface.blit(score_text, (10, self.ui_area_y + 10))
        
        # High score
        high_score_text = self.font_small.render(f"High Score: {score_info['high']}", True, LIGHT_GRAY)
        self.surface.blit(high_score_text, (10, self.ui_area_y + 55))
        
        # Snake length
        length_text = self.font_small.render(f"Length: {snake_length}", True, LIGHT_GRAY)
        self.surface.blit(length_text, (10, self.ui_area_y + 75))
        
        # Food eaten counter
        food_text = self.font_small.render(f"Food Eaten: {score_info['food_eaten']}", True, LIGHT_GRAY)
        self.surface.blit(food_text, (150, self.ui_area_y + 55))
        
        # Game status indicator
        status = "Playing" if game_state['current_state'] == "playing" else game_state['current_state'].title()
        status_color = GREEN if status == "Playing" else LIGHT_GRAY
        status_text = self.font_medium.render(f"Status: {status}", True, status_color)
        status_rect = status_text.get_rect()
        status_rect.right = WINDOW_WIDTH - 10
        status_rect.y = self.ui_area_y + 10
        self.surface.blit(status_text, status_rect)
    
    def _draw_game_over_overlay(self, score_info: Dict[str, Any]) -> None:
        """Draw game over overlay."""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, self.game_area_height))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.surface.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, self.game_area_height // 2 - 40))
        self.surface.blit(game_over_text, game_over_rect)
        
        # Final score
        final_score_text = self.font_medium.render(f"Final Score: {score_info['current']}", True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, self.game_area_height // 2))
        self.surface.blit(final_score_text, final_score_rect)
        
        # High score achievement
        if score_info['current'] == score_info['high'] and score_info['current'] > 0:
            new_high_text = self.font_small.render("🎉 NEW HIGH SCORE! 🎉", True, (255, 215, 0))  # Gold
            new_high_rect = new_high_text.get_rect(center=(WINDOW_WIDTH // 2, self.game_area_height // 2 + 30))
            self.surface.blit(new_high_text, new_high_rect)
        
        # Instructions
        instruction_text = self.font_small.render("Click 'Reset Game' to play again", True, LIGHT_GRAY)
        instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH // 2, self.game_area_height // 2 + 60))
        self.surface.blit(instruction_text, instruction_rect)
    
    def _draw_paused_overlay(self) -> None:
        """Draw paused overlay."""
        overlay = pygame.Surface((WINDOW_WIDTH, self.game_area_height))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.surface.blit(overlay, (0, 0))
        
        paused_text = self.font_large.render("PAUSED", True, WHITE)
        paused_rect = paused_text.get_rect(center=(WINDOW_WIDTH // 2, self.game_area_height // 2))
        self.surface.blit(paused_text, paused_rect)
    
    def _render_error(self, message: str) -> Image.Image:
        """Render error state."""
        self.surface.fill(BLACK)
        error_text = self.font_medium.render(f"Error: {message}", True, RED)
        error_rect = error_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.surface.blit(error_text, error_rect)
        return self._surface_to_pil_image()
    
    def _surface_to_pil_image(self) -> Image.Image:
        """Convert pygame surface to PIL Image."""
        # Get pixel array from surface
        pixel_array = pygame.surfarray.array3d(self.surface)
        
        # Pygame uses (width, height, 3) but PIL expects (height, width, 3)
        pixel_array = np.transpose(pixel_array, (1, 0, 2))
        
        # Convert to PIL Image
        image = Image.fromarray(pixel_array.astype(np.uint8))
        
        return image