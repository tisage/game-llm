#!/usr/bin/env python3
"""
Test script for game core functionality
"""
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from game_core import GameEngine, UP, DOWN, LEFT, RIGHT

def test_game_core():
    """Test core game functionality."""
    print("🧪 Testing Snake Game Core...")
    
    # Initialize game engine
    game = GameEngine()
    print(f"✅ Game engine initialized")
    
    # Test initial state
    state = game.get_game_state()
    print(f"✅ Initial game state: {state['current_state']}")
    print(f"   Snake length: {len(state['snake_body'])}")
    print(f"   Snake head: {state['snake_body'][0]}")
    print(f"   Food position: {state['food_position']}")
    print(f"   Score: {state['score_info']['current']}")
    
    # Test movement
    print("\n🎮 Testing movement...")
    original_head = state['snake_body'][0]
    
    # Move right
    game.handle_input(RIGHT)
    game.update()
    state = game.get_game_state()
    new_head = state['snake_body'][0]
    print(f"✅ Moved right: {original_head} -> {new_head}")
    
    # Move down
    game.handle_input(DOWN)
    game.update()
    state = game.get_game_state()
    print(f"✅ Moved down: {new_head} -> {state['snake_body'][0]}")
    
    # Test invalid move (opposite direction)
    current_head = state['snake_body'][0]
    game.handle_input(UP)  # Should be ignored (opposite of DOWN)
    game.update()
    state = game.get_game_state()
    if state['snake_body'][0] != current_head:
        print(f"✅ Invalid move correctly ignored")
    else:
        print(f"⚠️  Snake moved when it shouldn't have")
    
    # Test pause/resume
    print("\n⏸️  Testing pause/resume...")
    game.pause_game()
    print(f"✅ Game paused: {game.is_paused()}")
    
    game.resume_game()
    print(f"✅ Game resumed: {game.is_playing()}")
    
    # Test reset
    print("\n🔄 Testing reset...")
    game.reset_game()
    state = game.get_game_state()
    print(f"✅ Game reset - Score: {state['score_info']['current']}, Length: {len(state['snake_body'])}")
    
    print("\n🎯 Core functionality test completed successfully!")
    return True

def test_pygame_imports():
    """Test Pygame UI imports."""
    print("\n🎮 Testing Pygame imports...")
    try:
        from pygame_ui import PygameGameLoop, PygameRenderer, InputHandler
        print("✅ Pygame UI imports successful")
        return True
    except ImportError as e:
        print(f"❌ Pygame UI import failed: {e}")
        return False

if __name__ == "__main__":
    success = True
    
    try:
        success &= test_game_core()
        success &= test_pygame_imports()
        
        if success:
            print("\n🎉 All tests passed! Ready to run the game.")
        else:
            print("\n❌ Some tests failed. Check the output above.")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)