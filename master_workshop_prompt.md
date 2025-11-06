# 🎮 Single Master Prompt for Interactive Workshop

## The Complete Workshop Prompt

```
I'm conducting a 20-minute live workshop demonstration on AI-assisted game development. I want to build a Snake game step by step with your guidance, where you provide me with choices at each stage.

PROJECT CONSTRAINTS:
- Single Python file (snake_game.py)
- Python + Pygame only
- 600x400 window, 20x15 grid
- WASD controls for snake movement
- Basic collision detection (walls and self)
- Start with ONE food item that respawns
- Must work immediately when run

WORKSHOP WORKFLOW:
I want you to guide me through this process by offering me 2-3 choices at each decision point. After I make each choice, implement that choice and then offer the next set of options.

PHASE 1 - BASIC IMPLEMENTATION:
First, give me 2-3 different approaches for the basic Snake game structure:
- Option A: Simple procedural approach with minimal classes
- Option B: Object-oriented with Snake and Food classes  
- Option C: [Your suggestion]

For each option, briefly explain:
- Pros and cons for a live demo
- Implementation complexity
- Estimated time to complete

Wait for my choice, then implement the chosen approach with just the basics:
- Game window and main loop
- Snake that moves with WASD keys
- One food item that respawns when eaten
- Basic collision detection
- Score display

After implementation, TEST the code and tell me if it works, then move to Phase 2.

PHASE 2 - ENHANCEMENT SELECTION:
Once the basic game works, offer me 3 enhancement options:
- Visual improvements (colors, shapes, effects)
- Gameplay features (multiple food, speed changes, etc.)
- UI improvements (better score display, game over screen, etc.)

For each enhancement option, tell me:
- Visual impact for audience
- Implementation time (quick/medium/complex)
- Risk level (low/medium/high chance of breaking things)

After I choose, implement that enhancement and test it.

PHASE 3 - FINAL POLISH:
If time permits, offer me 2-3 quick polish options that would impress the audience:
- Simple visual effects that look professional
- Small gameplay tweaks
- UI improvements

Implement my final choice.

IMPORTANT RULES:
1. Always offer exactly 2-3 clear choices
2. Keep explanations brief (this is a live demo)
3. After each implementation, test the code and report if it works
4. If something doesn't work, immediately offer simpler alternatives
5. Remember this is for a live audience - prioritize things that LOOK impressive
6. Keep the code clean and readable
7. Always maintain backward compatibility (don't break existing features)

Ready? Start by giving me the 3 basic implementation approaches for the Snake game structure.
```