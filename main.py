#!/usr/bin/env python3
"""
Snake Game - Main Entry Point

This module provides different ways to run the Snake game:
1. Pygame version with WASD keyboard controls (default)
2. Gradio web interface version
3. Both versions simultaneously
"""

import argparse
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def run_pygame_version():
    """Run the Pygame version of Snake game."""
    try:
        from pygame_ui.game_loop import main
        print("🎮 Starting Pygame Snake Game...")
        print("Controls: W/A/S/D or Arrow Keys")
        print("Press R to restart when game over")
        print("Press P/Space to pause/resume")
        print("Press ESC to quit")
        print("Close window to exit")
        
        main()
    except ImportError as e:
        print(f"Error importing Pygame components: {e}")
        print("Make sure pygame is installed: pip install pygame")
        sys.exit(1)
    except Exception as e:
        print(f"Error running Pygame version: {e}")
        sys.exit(1)

def run_gradio_version(share=False, port=7860):
    """Run the Gradio web interface version."""
    try:
        from gradio_ui.web_interface import launch_gradio_interface
        print("🌐 Starting Gradio Snake Game Interface...")
        print(f"The web interface will be available at: http://localhost:{port}")
        
        launch_gradio_interface(share=share, port=port)
    except ImportError as e:
        print(f"Error importing Gradio components: {e}")
        print("Make sure gradio is installed: pip install gradio")
        sys.exit(1)
    except Exception as e:
        print(f"Error running Gradio version: {e}")
        sys.exit(1)

def run_both_versions():
    """Run both Pygame and Gradio versions simultaneously."""
    import threading
    import time
    
    print("🎮🌐 Starting both Pygame and Gradio versions...")
    
    # Start Gradio in a separate thread
    gradio_thread = threading.Thread(target=run_gradio_version, daemon=True)
    gradio_thread.start()
    
    # Give Gradio time to start up
    print("Starting Gradio web interface in background...")
    time.sleep(3)
    
    # Start Pygame in main thread
    print("Starting Pygame version in foreground...")
    run_pygame_version()

def main():
    """Main entry point with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Snake Game - Python, Pygame, and Gradio implementation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run Pygame version (default)
  python main.py --pygame           # Run Pygame version
  python main.py --gradio           # Run Gradio web interface
  python main.py --gradio --port 8080  # Run Gradio on custom port
  python main.py --gradio --share   # Run Gradio with public share link
  python main.py --both             # Run both versions

Game Features:
  - 20x15 grid
  - WASD key controls (Pygame) or button controls (Gradio)
  - Real-time movement (Pygame) or turn-based (Gradio)
  - Collision detection
  - Food consumption and scoring
  - Game over and restart functionality
  - High score tracking
        """
    )
    
    parser.add_argument(
        "--pygame", 
        action="store_true", 
        help="Run Pygame version with keyboard controls"
    )
    parser.add_argument(
        "--gradio", 
        action="store_true", 
        help="Run Gradio web interface version"
    )
    parser.add_argument(
        "--both", 
        action="store_true", 
        help="Run both Pygame and Gradio versions"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=7860, 
        help="Port for Gradio interface (default: 7860)"
    )
    parser.add_argument(
        "--share", 
        action="store_true", 
        help="Create public share link for Gradio interface"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="Snake Game v1.0"
    )
    
    args = parser.parse_args()
    
    # Determine which version to run
    if args.both:
        run_both_versions()
    elif args.gradio:
        run_gradio_version(share=args.share, port=args.port)
    elif args.pygame or not any([args.pygame, args.gradio, args.both]):
        # Default to Pygame if no specific option or --pygame is specified
        run_pygame_version()

if __name__ == "__main__":
    main()