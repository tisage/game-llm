# 🎯 Step-by-Step AI Prompts for Live Snake Game Development

**Workshop Format**: Interactive AI-assisted coding with GitHub Copilot CLI  
**Goal**: Build a working Snake game from scratch using AI prompts  
**Duration**: 30-45 minutes of live coding  
**Technology**: Pygame for real-time controls and simple graphics  
**Files to create**: `snake_game.py` (complete playable game)

---

## 🚀 Phase 1: Project Planning & Design (5 minutes)

### Prompt 1: Initial Project Discussion
```bash
gh copilot suggest "I want to build a Snake game using Python and Pygame for a CS workshop. It should have keyboard controls, real-time movement, and simple graphics. What should be the main components and architecture?"
```

**Expected AI Response**: Project structure, Pygame basics, main components  
**Your Role**: Discuss with students what AI suggests, ask follow-up questions

### Prompt 2: Game Requirements Refinement
```bash
gh copilot suggest "For the Pygame Snake game, I need: arrow key controls, 20x15 grid, real-time movement, collision detection, food consumption, and score display. What's the best code structure?"
```

**Expected AI Response**: Class design, game loop structure, Pygame concepts  
**Teaching Point**: Show how to refine requirements with AI

---

## 🐍 Phase 2: Core Game Logic Development (15 minutes)

### Prompt 3: Create Basic Pygame Structure
First, create `snake_game.py` in VS Code, then:

```bash
gh copilot suggest "Create a complete Snake game in Python using Pygame. Include: imports, constants (colors, screen size, cell size), Direction enum, SnakeGame class with __init__ method, and basic main game loop with pygame.init()."
```

**Expected AI Response**: Complete Pygame setup with basic structure  
**Action**: Type/paste the suggested code into `snake_game.py`

### Prompt 4: Implement Game Logic
```bash
gh copilot suggest "Complete the SnakeGame class with these methods: reset() to initialize game state, update() for game logic per frame, handle_input() for arrow keys, check_collision() for walls and self-collision, and place_food() for random food placement."
```

**Expected AI Response**: Complete game logic methods  
**Teaching Point**: Show how AI structures game logic

### Prompt 5: Add Rendering System
```bash
gh copilot suggest "Add a draw() method to SnakeGame that renders everything to the pygame screen: draw grid background, draw snake segments as rectangles, draw food, and display score text. Use simple colors and shapes."
```

**Expected AI Response**: Complete rendering system  
**Visual Result**: Students can see the game visually taking shape

### Prompt 6: Complete Game Loop
```bash
gh copilot suggest "Complete the main game loop that: handles pygame events (QUIT, KEYDOWN), calls game.handle_input(), calls game.update(), calls game.draw(), controls frame rate with pygame clock, and handles game over state."
```

**Expected AI Response**: Complete main loop with proper event handling  
**Testing**: The game should be playable at this point

### Prompt 7: Polish and Improvements
```bash
gh copilot suggest "Add these improvements to the Snake game: game over screen with restart option, better visual styling (borders, colors), smoother movement timing, and display of current score and high score."
```

**Expected AI Response**: Polish and enhancement suggestions  
**Student Engagement**: Let students suggest what to improve

---

## 🎮 Phase 3: Testing and Enhancement (10 minutes)

### Prompt 8: Test the Complete Game
```bash
gh copilot suggest "Add a test function that runs the Snake game, moves the snake a few times programmatically, and verifies all game mechanics work correctly. Also add command line options to run tests."
```

**Expected AI Response**: Testing and verification code  
**Live Demo**: Run the actual game for students to see

### Prompt 9: Add Game Features
```bash
gh copilot suggest "Add these features to the Pygame Snake game: pause functionality (spacebar), speed levels (1-5), grid lines for better visibility, and a start screen with instructions."
```

**Expected AI Response**: Feature enhancements  
**Student Input**: Ask students what features they want to see

### Prompt 10: Optimize and Polish
```bash
gh copilot suggest "Optimize the Snake game performance and add polish: smooth color transitions, better font rendering, sound effects using pygame.mixer, and improved game over animation."
```

**Expected AI Response**: Performance and visual improvements  
**Advanced Demo**: Show how AI can enhance existing code

---

## 🧪 Phase 4: Testing & Debugging (10 minutes)

### Prompt 11: Debug and Fix Issues
If there are problems, use prompts like:

```bash
gh copilot suggest "I'm getting [SPECIFIC ERROR MESSAGE] in my Pygame Snake game. How do I fix this?"
```

```bash
gh copilot suggest "The snake is not responding to arrow key presses properly. What could be wrong with the pygame event handling?"
```

```bash
gh copilot suggest "My Snake game is running too fast/slow. How do I control the game speed and frame rate in pygame?"
```

**Teaching Point**: Show how AI helps with debugging

### Prompt 13: Performance and Polish
```bash
gh copilot suggest "How can I improve the visual appearance and responsiveness of my Pygame Snake game? Suggest specific improvements for graphics, animations, and user experience."
```

**Expected AI Response**: Visual and performance improvements  
**Student Engagement**: Let students suggest features to add

---

## 🚀 Phase 5: Enhancement & Features (Optional - 10 minutes)

### Prompt 14: Add Advanced Features
```bash
gh copilot suggest "Add these advanced features to my Pygame Snake game: multiple difficulty levels, different game modes (classic, obstacles, time attack), power-ups, and a main menu system."
```

### Prompt 15: Create Modular Structure
```bash
gh copilot suggest "Refactor my Snake game into multiple files: game_logic.py for core game mechanics, graphics.py for rendering, and main.py as entry point. Keep it organized and educational."
```

### Prompt 16: Final Review and Documentation
```bash
gh copilot suggest "Review my complete Pygame Snake game and add: comprehensive comments for educational purposes, docstrings for all methods, and a README explaining how the code works for students."
```

---

## 🎓 Phase 6: Reflection & Discussion (5 minutes)

### Prompt 17: Code Analysis
```bash
gh copilot explain "Analyze the Snake game we just built. What programming concepts does it demonstrate? How does it show the benefits and limitations of AI-assisted coding?"
```

### Prompt 18: Next Steps
```bash
gh copilot suggest "What additional features could students add to this Snake game as homework assignments? Suggest 5 increasingly difficult enhancements."
```

---

## 🎯 Workshop Execution Tips

### For Each Prompt:
1. **Read the prompt aloud** to students
2. **Run the command** and show the AI response
3. **Discuss the suggestion** with students
4. **Type/implement** the code together
5. **Test frequently** to show progress

### Interactive Elements:
- **Ask students to suggest prompts** for features they want
- **Show failed prompts** and how to refine them
- **Let students vote** on which AI suggestions to implement
- **Demonstrate debugging** when things don't work perfectly

### Key Teaching Moments:
- **AI isn't magic**: Show when prompts need refinement
- **Human oversight**: Explain why we review AI suggestions
- **Iterative development**: Build features step by step
- **Modern workflow**: This is how professionals work with AI

### Technical Notes:
- **Save frequently**: After each working prompt
- **Test incrementally**: Don't wait until the end
- **Have backup code**: In case AI suggests something broken
- **Use VS Code**: Copilot integration works better than CLI alone

---

## 🔧 Troubleshooting Prompts

### If Pygame Won't Initialize:
```bash
gh copilot suggest "My Pygame won't initialize. I'm getting [ERROR]. How do I fix this and what are common Pygame setup issues?"
```

### If Controls Don't Work:
```bash
gh copilot suggest "The arrow keys aren't controlling my snake properly. Debug the pygame event handling and input system step by step."
```

### If Game Logic Fails:
```bash
gh copilot suggest "My snake game logic has a bug where [SPECIFIC ISSUE]. Debug this step by step and show me the fix."
```

### If Students Get Lost:
```bash
gh copilot suggest "Explain what this Pygame Snake game code does in simple terms for CS students. Break down the key concepts and how each part works."
```

### If Performance is Poor:
```bash
gh copilot suggest "My Pygame Snake game is running slowly or choppy. What are the most likely performance bottlenecks and how can I fix them?"
```

---

## 📋 Pre-Workshop Preparation

### Test These Prompts:
1. Run through the entire sequence once before the workshop
2. Note which prompts give the best responses
3. Prepare follow-up questions for common AI responses
4. Have backup code snippets for critical parts

### Prepare Your Environment:
- Empty folder with just `requirements.txt` (pygame, numpy)
- VS Code with Copilot extension active
- Terminal with `gh copilot` working
- Test that pygame works: `python -c "import pygame; print('Pygame ready!')"`

### Student Engagement:
- Prepare questions about each AI response
- Plan moments for student input and suggestions
- Have extension prompts ready for advanced students
- Prepare simple explanations for complex AI suggestions

---

**🎯 Remember**: The goal is to show the **conversation** between human and AI, not just code generation. Make it interactive and educational!

**🚀 Have fun demonstrating the future of programming!**