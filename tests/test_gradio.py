#!/usr/bin/env python3
"""
Test script for Gradio functionality
"""
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_gradio_imports():
    """Test Gradio imports and basic functionality."""
    print("🧪 Testing Gradio Snake Game Components...")
    
    try:
        # Test imports
        from gradio_ui import GradioSnakeGame, GameImageRenderer, ControlHandler
        from game_core import GameEngine
        print("✅ All Gradio imports successful")
        
        # Test game engine
        engine = GameEngine()
        print("✅ Game engine created")
        
        # Test image renderer
        renderer = GameImageRenderer()
        print("✅ Image renderer created")
        
        # Test control handler
        controller = ControlHandler(engine)
        print("✅ Control handler created")
        
        # Test game state rendering
        game_state = engine.get_game_state()
        image = renderer.render_game_state(game_state)
        print(f"✅ Game state rendered to image: {image.size}")
        
        # Test control actions
        status, success = controller.move_right()
        print(f"✅ Control action tested: {success}")
        
        # Test Gradio interface creation (without launching)
        game_interface = GradioSnakeGame()
        interface = game_interface.create_interface()
        print("✅ Gradio interface created successfully")
        
        print("\n🎉 All Gradio tests passed! Ready to launch web interface.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_quick_play():
    """Test a quick game sequence."""
    print("\n🎮 Testing quick game sequence...")
    
    try:
        from gradio_ui import GradioSnakeGame
        
        game = GradioSnakeGame()
        
        # Test movement sequence
        print("Testing movement sequence...")
        status, image = game.handle_right()
        print(f"  Right: {status}")
        
        status, image = game.handle_down()
        print(f"  Down: {status}")
        
        status, image = game.handle_left()
        print(f"  Left: {status}")
        
        # Test reset
        status, image = game.handle_reset()
        print(f"  Reset: {status}")
        
        print("✅ Quick play test completed")
        return True
        
    except Exception as e:
        print(f"❌ Quick play test failed: {e}")
        return False

if __name__ == "__main__":
    success = True
    
    try:
        success &= test_gradio_imports()
        success &= test_quick_play()
        
        if success:
            print("\n🎉 All Gradio tests passed!")
            print("\nTo launch the web interface, run:")
            print("  python main.py --gradio")
            print("  python main.py --gradio --port 8080")
            print("  python main.py --gradio --share")
        else:
            print("\n❌ Some tests failed. Check the output above.")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)