"""
Pygame renderer for Snake game
"""
import pygame
from typing import List, Tuple, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core.constants import *

class PygameRenderer:
    """Handles all Pygame rendering operations."""
    
    def __init__(self, screen: pygame.Surface):
        """Initialize renderer with pygame screen."""
        self.screen = screen
        
        # Initialize fonts
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # Game area rectangle (excluding UI area)
        self.game_area = pygame.Rect(0, 0, WINDOW_WIDTH, GRID_HEIGHT * CELL_SIZE)
        self.ui_area = pygame.Rect(0, GRID_HEIGHT * CELL_SIZE, WINDOW_WIDTH, 100)
    
    def render_frame(self, game_state: Dict[str, Any]) -> None:
        """Render complete game frame."""
        if not game_state.get('valid', False):
            self._render_error(game_state.get('message', 'Invalid game state'))
            return
        
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw game components
        self._draw_grid()
        self._draw_multiple_food(game_state)
        self._draw_snake(game_state['snake_body'])
        
        # Draw UI
        self._draw_ui(game_state)
        
        # Draw game state overlays
        if game_state['game_over']:
            self._draw_game_over(game_state['score_info'])
        elif game_state['paused']:
            self._draw_paused()
    
    def _draw_grid(self) -> None:
        """Draw grid lines for visual clarity."""
        # Vertical lines
        for x in range(0, WINDOW_WIDTH + 1, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, 
                           (x, 0), (x, GRID_HEIGHT * CELL_SIZE))
        
        # Horizontal lines
        for y in range(0, GRID_HEIGHT * CELL_SIZE + 1, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, 
                           (0, y), (WINDOW_WIDTH, y))
    
    def _draw_snake(self, snake_body: List[Tuple[int, int]]) -> None:
        """Draw snake on the screen."""
        for i, (x, y) in enumerate(snake_body):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            # Head is brighter green with special marking
            if i == 0:
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, WHITE, rect, 2)
                # Add eyes to head
                eye_size = 4
                eye1 = pygame.Rect(x * CELL_SIZE + 8, y * CELL_SIZE + 8, eye_size, eye_size)
                eye2 = pygame.Rect(x * CELL_SIZE + 18, y * CELL_SIZE + 8, eye_size, eye_size)
                pygame.draw.rect(self.screen, BLACK, eye1)
                pygame.draw.rect(self.screen, BLACK, eye2)
            else:
                # Body segments
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def _draw_food(self, food_position: Tuple[int, int], color: Tuple[int, int, int] = RED) -> None:
        """Draw a single food item with enhanced visual effects."""
        x, y = food_position
        center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
        radius = CELL_SIZE // 2 - 3
        
        # Draw shadow for depth
        shadow_center = (center[0] + 2, center[1] + 2)
        pygame.draw.circle(self.screen, (50, 50, 50), shadow_center, radius, 3)
        
        # Main food circle with gradient effect
        pygame.draw.circle(self.screen, color, center, radius)
        
        # Darker border for definition
        border_color = tuple(max(0, c - 50) for c in color)
        pygame.draw.circle(self.screen, border_color, center, radius, 2)
        
        # Bright highlight for 3D effect
        highlight_pos = (center[0] - radius//3, center[1] - radius//3)
        highlight_radius = radius // 3
        pygame.draw.circle(self.screen, WHITE, highlight_pos, highlight_radius)
        
        # Small sparkle effect
        sparkle_pos = (center[0] + radius//4, center[1] - radius//2)
        pygame.draw.circle(self.screen, WHITE, sparkle_pos, 2)
    
    def _draw_multiple_food(self, game_state: Dict[str, Any]) -> None:
        """Draw all food items on the screen with different colors."""
        # Check if we have new multiple food system
        if 'food_items' in game_state and game_state['food_items']:
            # Draw all food items with their individual colors
            for food_item in game_state['food_items']:
                self._draw_food(food_item.position, food_item.color)
        elif 'food_positions' in game_state and game_state['food_positions']:
            # Draw multiple positions with default colors
            colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]  # Red, Orange, Yellow
            for i, position in enumerate(game_state['food_positions']):
                color = colors[i % len(colors)]
                self._draw_food(position, color)
        else:
            # Fallback to single food
            self._draw_food(game_state['food_position'])
    
    def _draw_ui(self, game_state: Dict[str, Any]) -> None:
        """Draw user interface elements."""
        score_info = game_state['score_info']
        
        # Clear UI area
        pygame.draw.rect(self.screen, BLACK, self.ui_area)
        pygame.draw.line(self.screen, WHITE, 
                        (0, GRID_HEIGHT * CELL_SIZE), 
                        (WINDOW_WIDTH, GRID_HEIGHT * CELL_SIZE), 2)
        
        # Score display
        score_text = self.font_medium.render(f"Score: {score_info['current']}", True, WHITE)
        self.screen.blit(score_text, (10, GRID_HEIGHT * CELL_SIZE + 10))
        
        # High score
        high_score_text = self.font_small.render(f"High: {score_info['high']}", True, LIGHT_GRAY)
        self.screen.blit(high_score_text, (10, GRID_HEIGHT * CELL_SIZE + 45))
        
        # Length and food count
        length_text = self.font_small.render(f"Length: {len(game_state['snake_body'])}", True, LIGHT_GRAY)
        self.screen.blit(length_text, (10, GRID_HEIGHT * CELL_SIZE + 70))
        
        # Food count display
        food_count = len(game_state.get('food_positions', [game_state.get('food_position', (0,0))]))
        food_text = self.font_small.render(f"Food: {food_count}", True, LIGHT_GRAY)
        self.screen.blit(food_text, (150, GRID_HEIGHT * CELL_SIZE + 70))
        
        # Controls hint (updated for multiple food)
        controls_text = self.font_small.render("Multiple Food Mode! WASD=Move | R=Restart | P=Pause | ESC=Quit", True, LIGHT_GRAY)
        controls_rect = controls_text.get_rect()
        controls_rect.right = WINDOW_WIDTH - 10
        controls_rect.y = GRID_HEIGHT * CELL_SIZE + 10
        self.screen.blit(controls_text, controls_rect)
    
    def _draw_game_over(self, score_info: Dict[str, Any]) -> None:
        """Draw game over overlay."""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, GRID_HEIGHT * CELL_SIZE))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, GRID_HEIGHT * CELL_SIZE // 2 - 30))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        final_score_text = self.font_medium.render(f"Final Score: {score_info['current']}", True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, GRID_HEIGHT * CELL_SIZE // 2 + 10))
        self.screen.blit(final_score_text, final_score_rect)
        
        # Restart instruction
        restart_text = self.font_small.render("Press R to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, GRID_HEIGHT * CELL_SIZE // 2 + 40))
        self.screen.blit(restart_text, restart_rect)
    
    def _draw_paused(self) -> None:
        """Draw paused overlay."""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, GRID_HEIGHT * CELL_SIZE))
        overlay.set_alpha(120)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Paused text
        paused_text = self.font_large.render("PAUSED", True, WHITE)
        paused_rect = paused_text.get_rect(center=(WINDOW_WIDTH // 2, GRID_HEIGHT * CELL_SIZE // 2))
        self.screen.blit(paused_text, paused_rect)
        
        # Resume instruction
        resume_text = self.font_small.render("Press P to resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(WINDOW_WIDTH // 2, GRID_HEIGHT * CELL_SIZE // 2 + 30))
        self.screen.blit(resume_text, resume_rect)
    
    def _render_error(self, message: str) -> None:
        """Render error message."""
        self.screen.fill(BLACK)
        error_text = self.font_medium.render(f"Error: {message}", True, RED)
        error_rect = error_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(error_text, error_rect)