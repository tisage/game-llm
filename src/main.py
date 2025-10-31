"""
🚀 Snake Game - Main Application Entry Point
AI-Powered Game Development Workshop

This is the main file for launching the Snake game.
Perfect for VS Code demonstration and live coding.
"""

import sys
import os
import argparse

# Add src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import our game modules
from snake_game import SnakeGame, test_snake_game
from game_ui import launch_game, create_demo_interface

def main():
    """Main application entry point"""
    print("🎮 AI-Powered Snake Game Workshop")
    print("=" * 50)
    print("🎯 Built with GitHub Copilot CLI + Python + Gradio")
    print("📚 Educational demo for CS/AI students")
    print("=" * 50)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="AI-Powered Snake Game")
    parser.add_argument("--size", type=int, default=10, 
                       help="Grid size (default: 10)")
    parser.add_argument("--share", action="store_true", 
                       help="Create public Gradio link")
    parser.add_argument("--test", action="store_true", 
                       help="Run game logic tests only")
    parser.add_argument("--demo", action="store_true", 
                       help="Launch demo interface for workshop")
    
    args = parser.parse_args()
    
    # Handle test mode
    if args.test:
        print("🧪 Running game logic tests...")
        test_snake_game()
        return
    
    # Handle demo mode
    if args.demo:
        print("🎬 Launching workshop demo interface...")
        interface = create_demo_interface()
        interface.launch(share=args.share)
        return
    
    # Launch full game
    print(f"🚀 Launching Snake Game (Grid: {args.size}x{args.size})")
    print("💡 Use Ctrl+C to stop the server")
    print("🌐 Game will open in your browser automatically")
    
    try:
        launch_game(
            grid_size=args.size,
            share=args.share,
            debug=False
        )
    except KeyboardInterrupt:
        print("\n👋 Thanks for playing! Game stopped.")
    except Exception as e:
        print(f"❌ Error launching game: {e}")
        print("💡 Try running with --test flag to check game logic")

def workshop_demo():
    """
    Special function for live workshop demonstration
    Shows step-by-step game creation process
    """
    print("🎓 Workshop Demo Mode")
    print("📝 This demonstrates the AI-assisted development process")
    
    # Step 1: Test core game logic
    print("\n1️⃣ Testing core game logic...")
    test_snake_game()
    
    # Step 2: Create simple interface
    print("\n2️⃣ Creating Gradio interface...")
    interface = create_demo_interface()
    
    # Step 3: Launch for demonstration
    print("\n3️⃣ Launching for live demo...")
    interface.launch(share=False, quiet=True)

if __name__ == "__main__":
    main()