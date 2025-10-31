"""
🎮 Snake Game - Gradio User Interface
AI-Powered Game Development Workshop

This module creates the Gradio web interface for the Snake game.
Designed for live demonstration in VS Code and browser compatibility.
"""

import gradio as gr
import numpy as np
from PIL import Image
import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from snake_game import SnakeGame, Direction, GameState

class SnakeGameUI:
    """
    Gradio User Interface for Snake Game
    
    Provides web-based interface with:
    - Visual game board
    - Arrow button controls
    - Score display
    - Game status messages
    - Reset functionality
    """
    
    def __init__(self, grid_size: int = 10):
        """
        Initialize the game UI
        
        Args:
            grid_size (int): Size of the game grid
        """
        self.game = SnakeGame(grid_size)
        self.cell_size = 25  # Pixels per cell for display
        
    def reset_game(self):
        """
        Reset the game and return updated display
        
        Returns:
            Tuple: (image, status_text, score)
        """
        self.game.reset()
        return self._get_game_display()
    
    def move_snake(self, direction_str: str):
        """
        Move snake in specified direction
        
        Args:
            direction_str (str): Direction name ("up", "down", "left", "right")
            
        Returns:
            Tuple: (image, status_text, score)
        """
        # Map string to Direction enum
        direction_map = {
            "up": Direction.UP,
            "down": Direction.DOWN,
            "left": Direction.LEFT,
            "right": Direction.RIGHT
        }
        
        direction = direction_map.get(direction_str.lower())
        if direction:
            self.game.step(direction)
        
        return self._get_game_display()
    
    def auto_step(self):
        """
        Continue game in current direction (for auto-play mode)
        
        Returns:
            Tuple: (image, status_text, score)
        """
        self.game.step()
        return self._get_game_display()
    
    def _get_game_display(self):
        """
        Get current game state for display
        
        Returns:
            Tuple: (PIL Image, status string, score int)
        """
        # Get visual grid from game
        rgb_grid = self.game.get_visual_grid()
        
        # Calculate display size
        display_size = self.game.grid_size * self.cell_size
        
        # Convert to PIL Image and scale up
        image = Image.fromarray(rgb_grid, 'RGB')
        image = image.resize((display_size, display_size), Image.NEAREST)
        
        # Generate status message
        info = self.game.get_game_info()
        
        if self.game.state == GameState.NOT_STARTED:
            status = "🎮 Click any arrow button to start playing!"
        elif self.game.state == GameState.PLAYING:
            status = f"🐍 Playing... Score: {info['score']} | Snake Length: {info['snake_length']}"
        else:  # GAME_OVER
            status = f"💥 Game Over! Final Score: {info['score']} | Snake Length: {info['snake_length']}"
        
        return image, status, info['score']
    
    def create_interface(self):
        """
        Create and configure Gradio interface
        
        Returns:
            gr.Blocks: Configured Gradio interface
        """
        # Custom CSS for better appearance
        custom_css = """
        .game-container {
            max-width: 800px;
            margin: 0 auto;
        }
        .control-button {
            min-height: 50px;
            font-size: 20px;
        }
        .score-display {
            font-size: 18px;
            font-weight: bold;
        }
        """
        
        with gr.Blocks(
            title="🐍 AI-Powered Snake Game", 
            theme=gr.themes.Soft(),
            css=custom_css
        ) as interface:
            
            # Header
            gr.Markdown("# 🐍 AI-Powered Snake Game")
            gr.Markdown("*Built with GitHub Copilot CLI + Python + Gradio*")
            gr.Markdown("**Workshop Demo: From AI Prompts to Playable Game**")
            
            with gr.Row():
                # Left column: Game display
                with gr.Column(scale=2):
                    game_image = gr.Image(
                        label="🎮 Game Board",
                        type="pil",
                        interactive=False,
                        height=400,
                        width=400
                    )
                    
                # Right column: Controls and info
                with gr.Column(scale=1):
                    # Game status
                    status_text = gr.Textbox(
                        label="📊 Game Status",
                        interactive=False,
                        lines=2,
                        elem_classes=["score-display"]
                    )
                    
                    # Score display
                    score_display = gr.Number(
                        label="🏆 Score",
                        value=0,
                        interactive=False,
                        elem_classes=["score-display"]
                    )
                    
                    # Control buttons
                    gr.Markdown("### 🎮 Controls")
                    
                    # Arrow button layout
                    with gr.Row():
                        gr.Column(scale=1)  # Spacer
                        up_btn = gr.Button(
                            "⬆️", 
                            elem_classes=["control-button"],
                            size="sm"
                        )
                        gr.Column(scale=1)  # Spacer
                    
                    with gr.Row():
                        left_btn = gr.Button(
                            "⬅️", 
                            elem_classes=["control-button"],
                            size="sm"
                        )
                        reset_btn = gr.Button(
                            "🔄 Reset", 
                            variant="secondary",
                            elem_classes=["control-button"]
                        )
                        right_btn = gr.Button(
                            "➡️", 
                            elem_classes=["control-button"],
                            size="sm"
                        )
                    
                    with gr.Row():
                        gr.Column(scale=1)  # Spacer
                        down_btn = gr.Button(
                            "⬇️", 
                            elem_classes=["control-button"],
                            size="sm"
                        )
                        gr.Column(scale=1)  # Spacer
                    
                    # Auto-play section
                    gr.Markdown("### 🤖 Auto Mode")
                    auto_btn = gr.Button(
                        "▶️ Auto Step", 
                        variant="primary",
                        elem_classes=["control-button"]
                    )
                    
                    # Workshop info
                    gr.Markdown("### 📚 Workshop Info")
                    gr.Markdown(
                        "This game demonstrates AI-assisted development using:\n"
                        "- **GitHub Copilot CLI** for code generation\n"
                        "- **VS Code** for development\n"
                        "- **Python + Gradio** for rapid prototyping"
                    )
            
            # Event handlers
            def move_up():
                return self.move_snake("up")
            
            def move_down():
                return self.move_snake("down")
            
            def move_left():
                return self.move_snake("left")
            
            def move_right():
                return self.move_snake("right")
            
            # Bind button events
            outputs = [game_image, status_text, score_display]
            
            up_btn.click(move_up, outputs=outputs)
            down_btn.click(move_down, outputs=outputs)
            left_btn.click(move_left, outputs=outputs)
            right_btn.click(move_right, outputs=outputs)
            reset_btn.click(self.reset_game, outputs=outputs)
            auto_btn.click(self.auto_step, outputs=outputs)
            
            # Initialize display on load
            interface.load(self.reset_game, outputs=outputs)
        
        return interface

def launch_game(grid_size: int = 10, share: bool = False, debug: bool = False):
    """
    Launch the Snake game interface
    
    Args:
        grid_size (int): Size of the game grid
        share (bool): Whether to create public link
        debug (bool): Enable debug mode
    """
    print("🐍 Launching AI-Powered Snake Game...")
    print(f"📏 Grid size: {grid_size}x{grid_size}")
    print("🎯 Perfect for workshop demonstration!")
    
    # Create UI instance
    ui = SnakeGameUI(grid_size)
    interface = ui.create_interface()
    
    # Launch with appropriate settings
    interface.launch(
        share=share,
        server_name="0.0.0.0" if not debug else "127.0.0.1",
        show_error=True,
        quiet=False
    )

# Gradio Interface Creation Helper for Copilot Demo
def create_demo_interface():
    """
    Quick demo interface creation for live coding demonstration
    """
    print("🎬 Creating demo interface for workshop...")
    
    # Simple version for step-by-step building
    ui = SnakeGameUI(grid_size=8)  # Smaller grid for demo
    return ui.create_interface()

if __name__ == "__main__":
    # Launch game with default settings
    launch_game(grid_size=10, share=False, debug=True)