#!/usr/bin/env python3
"""
Comprehensive test suite for Snake Game core functionality
"""
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_collision_detection():
    """Test various collision scenarios."""
    print("🔍 Testing collision detection...")
    
    try:
        from game_core.collision import CollisionDetector
        
        # Test wall collisions
        assert CollisionDetector.check_wall_collision((-1, 5), 20, 15), "Left wall collision"
        assert CollisionDetector.check_wall_collision((20, 5), 20, 15), "Right wall collision"
        assert CollisionDetector.check_wall_collision((5, -1), 20, 15), "Top wall collision"
        assert CollisionDetector.check_wall_collision((5, 15), 20, 15), "Bottom wall collision"
        assert not CollisionDetector.check_wall_collision((10, 7), 20, 15), "Valid position"
        
        # Test self collision
        snake_body = [(10, 7), (9, 7), (8, 7), (8, 8), (9, 8), (10, 8)]
        assert CollisionDetector.check_self_collision((9, 7), snake_body), "Self collision"
        assert not CollisionDetector.check_self_collision((11, 7), snake_body), "No self collision"
        
        # Test food collision
        assert CollisionDetector.check_food_collision((5, 5), (5, 5)), "Food collision"
        assert not CollisionDetector.check_food_collision((5, 5), (6, 5)), "No food collision"
        
        print("✅ All collision detection tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Collision detection test failed: {e}")
        return False

def test_scoring_system():
    """Test scoring and high score functionality."""
    print("📊 Testing scoring system...")
    
    try:
        from game_core.scoring import ScoreManager
        
        score_manager = ScoreManager()
        
        # Test initial state
        assert score_manager.get_current_score() == 0, "Initial score should be 0"
        assert score_manager.get_high_score() == 0, "Initial high score should be 0"
        assert score_manager.get_food_eaten() == 0, "Initial food eaten should be 0"
        
        # Test scoring
        score_manager.add_food_score()
        assert score_manager.get_current_score() == 10, "Score should be 10 after one food"
        assert score_manager.get_high_score() == 10, "High score should update"
        assert score_manager.get_food_eaten() == 1, "Food eaten should be 1"
        
        # Test reset
        score_manager.reset_current_game()
        assert score_manager.get_current_score() == 0, "Current score should reset"
        assert score_manager.get_high_score() == 10, "High score should persist"
        
        print("✅ Scoring system tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Scoring system test failed: {e}")
        return False

def test_complete_game_session():
    """Test a complete game session with multiple actions."""
    print("🎮 Testing complete game session...")
    
    try:
        from game_core import GameEngine, UP, DOWN, LEFT, RIGHT
        
        game = GameEngine()
        
        # Test initial state
        state = game.get_game_state()
        assert state['valid'], "Game state should be valid"
        assert state['score_info']['current'] == 0, "Initial score should be 0"
        assert len(state['snake_body']) == 3, "Initial snake length should be 3"
        
        # Test movement sequence
        moves = [RIGHT, RIGHT, DOWN, DOWN, LEFT, LEFT, UP, UP]
        for i, move in enumerate(moves):
            game.handle_input(move)
            update_info = game.update()
            
            if update_info['game_ended']:
                print(f"✅ Game ended after {i+1} moves (collision detected)")
                break
            elif update_info['food_eaten']:
                print(f"✅ Food eaten at move {i+1}, score: {update_info['score']}")
        
        print("✅ Complete game session test passed")
        return True
        
    except Exception as e:
        print(f"❌ Complete game session test failed: {e}")
        return False

def test_pygame_components():
    """Test Pygame UI components."""
    print("🎮 Testing Pygame components...")
    
    try:
        from pygame_ui import PygameRenderer, InputHandler
        from game_core import GameEngine
        import pygame
        
        # Initialize pygame
        pygame.init()
        screen = pygame.Surface((600, 550))
        
        # Test renderer
        renderer = PygameRenderer(screen)
        game = GameEngine()
        game_state = game.get_game_state()
        
        # This should not crash
        renderer.render_frame(game_state)
        
        # Test input handler
        input_handler = InputHandler()
        assert not input_handler.is_quit_requested(), "No quit initially"
        assert not input_handler.is_restart_requested(), "No restart initially"
        
        print("✅ Pygame components test passed")
        return True
        
    except Exception as e:
        print(f"❌ Pygame components test failed: {e}")
        return False

def run_all_tests():
    """Run all test suites."""
    print("🧪 Running comprehensive Snake Game test suite...\n")
    
    tests = [
        test_collision_detection,
        test_scoring_system,
        test_complete_game_session,
        test_pygame_components,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Add spacing between tests
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}\n")
    
    print(f"📋 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Snake Game is ready to play!")
        print("\nTo run the game: python main.py")
        return True
    else:
        print(f"❌ {total - passed} tests failed. Check the output above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)