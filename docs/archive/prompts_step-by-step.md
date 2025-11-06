# 🐍 Snake Game Development - Step-by-Step Prompts

**Purpose**: AI Workshop Demo - Complete prompt sequence to build a working Snake game from scratch  
**Target**: Reproducible prompts that generate a functional Snake game with multiple food items  
**Expected Result**: 15+ Python files, ~1300 lines of code, fully playable game  

---

## Phase 1: Idea & Architecture Planning

### Prompt 1.1: Initial Concept & Requirements
```
I want to build a Snake game using Python and Pygame. It should have keyboard controls, real-time movement, and simple graphics. What should be the main components and architecture?

For the Snake game, I need:
- WASD key controls
- 20x15 grid
- Real-time movement
- Collision detection
- Food consumption and growth
- Score display

Don't show me code for now. I need to discuss the design, framework, and architecture first.
```

### Prompt 1.2: Architecture Confirmation & Setup
```
I'm using .venv for virtual environment. Your logic looks good. 

Can you start the code implementation with:
- Backend code in `src/game_core/` folder for pure game logic
- Frontend code in `src/pygame_ui/` folder for the interface
- Provide all necessary setup including requirements.txt file
- Test your code after every major implementation

Please create the project structure and implement the core components.
```

---

## Phase 2: Initial Implementation & Testing

### Prompt 2.1: Core Implementation Request
```
Please implement the complete Snake game with the following structure:

1. Create requirements.txt with all dependencies
2. Implement game_core modules: constants, snake, food, collision, scoring, game_state
3. Implement pygame_ui modules: renderer, input_handler, game_loop
4. Create main.py as entry point
5. Include test files

Make sure WASD controls work properly and the game is fully playable.
```

### Prompt 2.2: Testing & Validation
```
Create comprehensive tests to verify:
- Snake movement and growth
- Collision detection (walls and self)
- Food spawning and consumption
- Score tracking
- Game state management

Also create a test script that validates the complete game functionality.
```

---

## Phase 3: Debugging & Control Issues

### Prompt 3.1: WASD Control Debug
```
When I run the game, the WASD keys are not moving the snake. Can you help me debug this issue?

The game window opens but pressing W/A/S/D keys doesn't make the snake move. Please check:
- Input handling implementation
- Event processing
- Movement timing
- Window focus issues

Provide debug solutions and fix the control problems.
```

### Prompt 3.2: Movement System Fix
```
The controls are still not working properly. Please review and fix:
- Make sure key events are properly captured
- Ensure immediate response to WASD input
- Fix any timing issues with movement
- Add debug output to verify key presses are detected

I want smooth, responsive WASD controls that work immediately when pressed.
```

---

## Phase 4: Code Cleanup & Simplification

### Prompt 4.1: Project Cleanup
```
Let's clean up the project and focus on a simple, working Pygame implementation:

1. Remove any unnecessary files or complexity
2. Keep only the core Pygame implementation that works
3. Ensure WASD controls are perfectly functional
4. Simplify requirements.txt to only essential packages
5. Focus on clean, maintainable code structure

The goal is a simple but working Snake game with great controls.
```

### Prompt 4.2: Validation & Polish
```
Please verify that the cleaned-up version:
- Has working WASD controls with immediate response
- Runs without errors
- Has proper collision detection
- Shows score correctly
- Has clean, professional code structure

Fix any remaining issues and ensure the game is fully playable.
```

---

## Phase 5: Visual Enhancement & Multiple Food

### Prompt 5.1: Multiple Food Implementation
```
Now I want to enhance the game by adding multiple food items on the board simultaneously.

Please implement:
- 2-3 food items on the board at the same time
- Different colors for each food item (red, orange, yellow, pink, purple)
- Smart positioning that avoids snake body and other food
- Automatic respawning when food is eaten
- Enhanced visual effects (3D style, shadows, highlights)

Keep the same WASD controls and game mechanics, just add multiple colorful food.
```

### Prompt 5.2: Visual Polish & Effects
```
Enhance the visual appearance of the food items:
- Make food look 3D with shadows and highlights
- Add sparkle effects for visual appeal
- Use gradient colors and professional styling
- Improve the overall game appearance
- Add food counter in the UI
- Make the game look polished and professional

The goal is to make the food items look attractive and the game visually appealing.
```

---

## Phase 6: Final Testing & Validation

### Prompt 6.1: Complete System Test
```
Please create a comprehensive test to verify the final game:
- Test all WASD controls work perfectly
- Verify multiple food system functions correctly
- Check visual effects render properly
- Ensure no crashes or bugs
- Validate score tracking and game over scenarios

Create both automated tests and manual testing instructions.
```

### Prompt 6.2: Final Cleanup & Documentation
```
Prepare the final version for demo:
- Clean up any debug files or temporary code
- Ensure main.py runs the game immediately
- Create a simple launch script (snake_enhanced.py)
- Verify all files are properly organized
- Test that the game works from a fresh installation

The final product should be ready for demonstration with working WASD controls and multiple colorful food items.
```

---

## Expected Final Structure
```
snake-game/
├── main.py                    # Basic entry point
├── snake_enhanced.py          # Enhanced version
├── requirements.txt           # pygame>=2.5.0, pytest>=7.0.0
├── src/
│   ├── game_core/            # 7 Python files
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── snake.py
│   │   ├── food.py           # Multiple food system
│   │   ├── collision.py
│   │   ├── scoring.py
│   │   └── game_state.py
│   └── pygame_ui/            # 3 Python files
│       ├── __init__.py
│       ├── game_loop.py
│       ├── input_handler.py
│       └── renderer.py       # Enhanced visuals
└── tests/                    # 2 test files
    ├── test_core.py
    └── test_complete.py
```

## Success Criteria
- ✅ WASD controls work immediately and smoothly
- ✅ 2-3 colorful food items on board simultaneously
- ✅ Enhanced 3D visual effects with shadows and sparkles
- ✅ Professional code architecture (15 files, ~1300 lines)
- ✅ No crashes, complete game functionality
- ✅ Ready for live demo presentation

## Usage for Workshop Demo
1. Use prompts in exact sequence with AI assistant
2. Test each phase before proceeding to next
3. Expect ~2-3 hours total development time
4. Final result: Professional Snake game ready for demo