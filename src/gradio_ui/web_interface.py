"""
Gradio web interface for Snake game
"""
import gradio as gr
from typing import Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_core import GameEngine
from .image_renderer import GameImageRenderer
from .control_handler import ControlHandler

class GradioSnakeGame:
    """Main Gradio interface for Snake game."""
    
    def __init__(self):
        """Initialize Gradio Snake game interface."""
        # Core components
        self.game_engine = GameEngine()
        self.image_renderer = GameImageRenderer()
        self.control_handler = ControlHandler(self.game_engine)
        
        # Initialize game
        self.game_engine.start_game()
        
        print("🌐 Gradio Snake Game initialized!")
    
    def get_current_display(self) -> Tuple[str, gr.Image]:
        """Get current game display and status."""
        game_state = self.game_engine.get_game_state()
        image = self.image_renderer.render_game_state(game_state)
        status = self.control_handler._get_status_message()
        
        return status, image
    
    def handle_up(self) -> Tuple[str, gr.Image]:
        """Handle up movement."""
        status, success = self.control_handler.move_up()
        _, image = self.get_current_display()
        return status, image
    
    def handle_down(self) -> Tuple[str, gr.Image]:
        """Handle down movement."""
        status, success = self.control_handler.move_down()
        _, image = self.get_current_display()
        return status, image
    
    def handle_left(self) -> Tuple[str, gr.Image]:
        """Handle left movement."""
        status, success = self.control_handler.move_left()
        _, image = self.get_current_display()
        return status, image
    
    def handle_right(self) -> Tuple[str, gr.Image]:
        """Handle right movement."""
        status, success = self.control_handler.move_right()
        _, image = self.get_current_display()
        return status, image
    
    def handle_start(self) -> Tuple[str, gr.Image]:
        """Handle start game."""
        status = self.control_handler.start_game()
        _, image = self.get_current_display()
        return status, image
    
    def handle_pause(self) -> Tuple[str, gr.Image]:
        """Handle pause/resume."""
        status = self.control_handler.pause_game()
        _, image = self.get_current_display()
        return status, image
    
    def handle_reset(self) -> Tuple[str, gr.Image]:
        """Handle reset game."""
        status = self.control_handler.reset_game()
        _, image = self.get_current_display()
        return status, image
    
    def create_interface(self) -> gr.Blocks:
        """Create the Gradio interface."""
        # Custom CSS for better styling
        custom_css = """
        .game-container {
            max-width: 800px;
            margin: 0 auto;
        }
        .control-button {
            min-height: 60px;
            font-size: 18px;
            font-weight: bold;
        }
        .direction-btn {
            min-height: 80px;
            font-size: 24px;
        }
        .status-text {
            font-family: 'Courier New', monospace;
            font-size: 16px;
        }
        """
        
        with gr.Blocks(
            title="🐍 Snake Game", 
            theme=gr.themes.Soft(), 
            css=custom_css
        ) as interface:
            
            gr.Markdown("""
            # 🐍 Snake Game
            ### Classic Snake game with modern web controls!
            
            **How to play:**
            - Use the directional buttons (W/A/S/D) to control your snake
            - Eat the red food 🍎 to grow and score points
            - Avoid hitting walls or yourself
            - Try to beat your high score!
            """)
            
            with gr.Row(elem_classes="game-container"):
                with gr.Column(scale=3):
                    # Game display
                    game_image = gr.Image(
                        label="Game Display",
                        show_label=False,
                        height=500,
                        width=600,
                        interactive=False
                    )
                    
                with gr.Column(scale=2):
                    # Status display
                    status_text = gr.Textbox(
                        label="Game Status",
                        value="🟢 Ready to play!",
                        interactive=False,
                        lines=3,
                        elem_classes="status-text"
                    )
                    
                    # Game controls
                    gr.Markdown("### 🎮 Game Controls")
                    with gr.Row():
                        start_btn = gr.Button("🎮 Start New Game", variant="primary", elem_classes="control-button")
                        pause_btn = gr.Button("⏸️ Pause/Resume", elem_classes="control-button")
                        reset_btn = gr.Button("🔄 Reset", elem_classes="control-button")
                    
                    # Movement controls
                    gr.Markdown("### 🕹️ Movement Controls")
                    with gr.Column():
                        # Up button
                        up_btn = gr.Button("⬆️ W (Up)", elem_classes="direction-btn")
                        
                        # Left, Down, Right buttons
                        with gr.Row():
                            left_btn = gr.Button("⬅️ A (Left)", elem_classes="direction-btn")
                            down_btn = gr.Button("⬇️ S (Down)", elem_classes="direction-btn")
                            right_btn = gr.Button("➡️ D (Right)", elem_classes="direction-btn")
                    
                    # Game stats
                    gr.Markdown("### 📊 Game Info")
                    gr.Markdown("""
                    - **Grid Size:** 20 × 15
                    - **Scoring:** 10 points per food
                    - **Growth:** Snake grows with each food
                    - **Speed:** Turn-based (click to move)
                    """)
                    
                    # Tips
                    gr.Markdown("### 💡 Tips")
                    gr.Markdown("""
                    - Plan your moves carefully
                    - Try to create loops for safety
                    - Corner yourself? Use Reset!
                    - Beat your high score! 🏆
                    """)
            
            # Event handlers
            start_btn.click(
                fn=self.handle_start,
                outputs=[status_text, game_image]
            )
            
            pause_btn.click(
                fn=self.handle_pause,
                outputs=[status_text, game_image]
            )
            
            reset_btn.click(
                fn=self.handle_reset,
                outputs=[status_text, game_image]
            )
            
            up_btn.click(
                fn=self.handle_up,
                outputs=[status_text, game_image]
            )
            
            down_btn.click(
                fn=self.handle_down,
                outputs=[status_text, game_image]
            )
            
            left_btn.click(
                fn=self.handle_left,
                outputs=[status_text, game_image]
            )
            
            right_btn.click(
                fn=self.handle_right,
                outputs=[status_text, game_image]
            )
            
            # Load initial display
            interface.load(
                fn=self.get_current_display,
                outputs=[status_text, game_image]
            )
        
        return interface

def launch_gradio_interface(share: bool = False, port: int = 7860):
    """Launch the Gradio interface."""
    print("🚀 Starting Gradio Snake Game Interface...")
    
    # Create game instance
    game_interface = GradioSnakeGame()
    interface = game_interface.create_interface()
    
    print(f"🌐 Starting web server on port {port}...")
    if share:
        print("🔗 Creating public share link...")
    
    # Launch interface
    interface.launch(
        server_name="0.0.0.0",
        server_port=port,
        share=share,
        show_error=True,
        quiet=False
    )

if __name__ == "__main__":
    launch_gradio_interface()