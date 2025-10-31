#!/usr/bin/env python3
"""
Simple input test for Snake Game
"""
import pygame
import sys

def simple_input_test():
    """Ultra-simple input test."""
    print("🔍 Simple Input Test")
    print("=" * 30)
    print("1. A small window will open")
    print("2. Click on the window to focus it")
    print("3. Press WASD keys to test")
    print("4. Press ESC to exit")
    print("=" * 30)
    
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("🎮 WASD Test - Click here first!")
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()
    
    running = True
    last_key = "None"
    key_count = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                print(f"✅ Key detected: {key_name}")
                
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                    last_key = key_name.upper()
                    key_count += 1
                    print(f"🎯 WASD key: {last_key}")
                else:
                    last_key = key_name
                    key_count += 1
        
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Instructions
        title = font.render("WASD Input Test", True, (255, 255, 255))
        screen.blit(title, (100, 50))
        
        instruction = small_font.render("Click window, then press WASD", True, (200, 200, 200))
        screen.blit(instruction, (80, 100))
        
        # Last key pressed
        key_text = font.render(f"Last: {last_key}", True, (0, 255, 0))
        screen.blit(key_text, (120, 150))
        
        # Count
        count_text = small_font.render(f"Keys pressed: {key_count}", True, (200, 200, 200))
        screen.blit(count_text, (130, 200))
        
        # Exit instruction
        exit_text = small_font.render("Press ESC to exit", True, (255, 100, 100))
        screen.blit(exit_text, (130, 250))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    
    if key_count > 0:
        print(f"✅ Input test successful! {key_count} keys detected.")
        print("Your keyboard input is working with Pygame.")
        print("If Snake game still doesn't respond, the issue is in the game logic.")
    else:
        print("❌ No keys detected.")
        print("Possible issues:")
        print("- Window didn't have focus")
        print("- Pygame input not working on this system")
        print("- Keyboard/system conflict")

if __name__ == "__main__":
    simple_input_test()