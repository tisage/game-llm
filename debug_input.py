#!/usr/bin/env python3
"""
Debug version of Pygame Snake game to test input handling
"""
import pygame
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from game_core import GameEngine, UP, DOWN, LEFT, RIGHT
from game_core.constants import *

def debug_input_test():
    """Test input handling in isolation."""
    print("🔍 Testing input handling...")
    
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Input Debug Test")
    clock = pygame.time.Clock()
    
    # Key mapping
    key_map = {
        pygame.K_w: UP,
        pygame.K_a: LEFT,
        pygame.K_s: DOWN,
        pygame.K_d: RIGHT,
        pygame.K_UP: UP,
        pygame.K_LEFT: LEFT,
        pygame.K_DOWN: DOWN,
        pygame.K_RIGHT: RIGHT
    }
    
    running = True
    last_key = "None"
    
    print("Press WASD or Arrow keys. Press ESC to quit.")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in key_map:
                    direction = key_map[event.key]
                    direction_names = {UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT"}
                    key_name = pygame.key.name(event.key).upper()
                    direction_name = direction_names[direction]
                    print(f"✅ Key pressed: {key_name} -> Direction: {direction_name}")
                    last_key = f"{key_name} ({direction_name})"
        
        # Clear screen
        screen.fill(BLACK)
        
        # Display last key
        font = pygame.font.Font(None, 36)
        text = font.render(f"Last key: {last_key}", True, WHITE)
        screen.blit(text, (10, 10))
        
        instructions = font.render("Press WASD or Arrow keys", True, WHITE)
        screen.blit(instructions, (10, 60))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("🔍 Input test completed.")

def debug_game_with_verbose_output():
    """Run the game with verbose debug output."""
    print("🎮 Starting debug game with verbose output...")
    
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game - Debug Mode")
    clock = pygame.time.Clock()
    
    # Initialize game
    game_engine = GameEngine()
    game_engine.start_game()
    
    # Key mapping
    key_map = {
        pygame.K_w: UP,
        pygame.K_a: LEFT,
        pygame.K_s: DOWN,
        pygame.K_d: RIGHT,
        pygame.K_UP: UP,
        pygame.K_LEFT: LEFT,
        pygame.K_DOWN: DOWN,
        pygame.K_RIGHT: RIGHT
    }
    
    running = True
    move_count = 0
    last_move_time = 0
    
    print("🎮 Debug mode active. Watch console for detailed output.")
    print("Controls: WASD or Arrow keys")
    
    while running:
        current_time = pygame.time.get_ticks()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    print("🔄 Restarting game...")
                    game_engine.start_game()
                    move_count = 0
                elif event.key in key_map:
                    direction = key_map[event.key]
                    direction_names = {UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT"}
                    key_name = pygame.key.name(event.key).upper()
                    direction_name = direction_names[direction]
                    
                    print(f"🎯 Input: {key_name} -> {direction_name}")
                    
                    if game_engine.is_playing():
                        success = game_engine.handle_input(direction)
                        if success:
                            print(f"✅ Direction change accepted: {direction_name}")
                            update_info = game_engine.update()
                            move_count += 1
                            
                            game_state = game_engine.get_game_state()
                            head_pos = game_state['snake_body'][0]
                            print(f"📍 Move #{move_count}: Snake head at {head_pos}")
                            
                            if update_info['food_eaten']:
                                print(f"🍎 Food eaten! Score: {update_info['score']}")
                            if update_info['game_ended']:
                                print(f"💥 Game Over! Final Score: {update_info['score']}")
                        else:
                            print(f"❌ Direction change rejected (invalid move)")
                    else:
                        print(f"⏸️ Game not playing (state: {game_engine.current_state})")
        
        # Automatic movement (less frequent)
        if current_time - last_move_time >= INITIAL_SNAKE_SPEED:
            if game_engine.is_playing():
                print(f"⏰ Automatic update at {current_time}ms")
                update_info = game_engine.update()
                if update_info['game_ended']:
                    print(f"💥 Game Over from automatic movement!")
            last_move_time = current_time
        
        # Simple rendering
        screen.fill(BLACK)
        
        if game_engine.is_playing() or game_engine.is_game_over():
            game_state = game_engine.get_game_state()
            
            # Draw snake
            for i, (x, y) in enumerate(game_state['snake_body']):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = GREEN if i == 0 else DARK_GREEN
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)
            
            # Draw food
            food_x, food_y = game_state['food_position']
            food_rect = pygame.Rect(food_x * CELL_SIZE, food_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, RED, food_rect)
            
            # Draw score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {game_state['score_info']['current']}", True, WHITE)
            screen.blit(score_text, (10, GRID_HEIGHT * CELL_SIZE + 10))
            
            move_text = font.render(f"Moves: {move_count}", True, WHITE)
            screen.blit(move_text, (10, GRID_HEIGHT * CELL_SIZE + 40))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("🎮 Debug game ended.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Debug Snake Game Input")
    parser.add_argument("--input-test", action="store_true", help="Test input handling only")
    parser.add_argument("--game-debug", action="store_true", help="Run game with debug output")
    
    args = parser.parse_args()
    
    if args.input_test:
        debug_input_test()
    elif args.game_debug:
        debug_game_with_verbose_output()
    else:
        print("Choose an option:")
        print("  --input-test   : Test keyboard input detection")
        print("  --game-debug   : Run game with verbose debug output")