#!/usr/bin/env python3
"""
Snake Game - Pygame Version

Simple Snake game implementation using Pygame with WASD controls.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def main():
    """Main entry point."""
    try:
        from pygame_ui.game_loop import main as pygame_main
        print("🎮 Starting Snake Game...")
        print("Controls: W/A/S/D or Arrow Keys")
        print("Press R to restart, P to pause, ESC to quit")
        
        pygame_main()
    except ImportError as e:
        print(f"Error importing Pygame components: {e}")
        print("Make sure pygame is installed: pip install pygame")
        sys.exit(1)
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()