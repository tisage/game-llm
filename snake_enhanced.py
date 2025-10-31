#!/usr/bin/env python3
"""
Enhanced Snake Game with Multiple Food Items
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def main():
    """Main entry point for enhanced Snake game."""
    try:
        from pygame_ui.game_loop import main as pygame_main
        print("🐍 Starting Enhanced Snake Game with Multiple Food!")
        print("✨ Features:")
        print("   - Multiple colorful food items on board")
        print("   - Enhanced visual effects")
        print("   - Same great WASD controls")
        print("\n🎮 Controls:")
        print("   W/A/S/D or Arrow Keys - Move snake")
        print("   R - Restart game")
        print("   P/Space - Pause/Resume") 
        print("   ESC - Quit game")
        print("\n🍎 Eat all the colorful food to grow and score!")
        
        pygame_main()
    except ImportError as e:
        print(f"Error importing game components: {e}")
        print("Make sure pygame is installed: pip install pygame")
        sys.exit(1)
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()