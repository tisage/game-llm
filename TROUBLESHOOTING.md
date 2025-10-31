# 🐛 Snake Game WASD Input Troubleshooting Guide

## 🎯 Common Issues and Solutions

### Issue: Snake not responding to WASD keys

**Most Common Cause: Window Focus**
1. **Click on the game window** to give it focus
2. Make sure the Pygame window is the active/foreground window
3. Try pressing keys only after clicking in the game area

### Debugging Steps:

#### Step 1: Test Basic Input Detection
```bash
python debug_input.py --input-test
```
This will open a simple window that shows which keys are being detected.

#### Step 2: Test Game with Debug Output
```bash
python debug_input.py --game-debug
```
This runs the game with verbose console output showing all input events.

#### Step 3: Check Pygame Installation
```bash
python -c "import pygame; print(f'Pygame version: {pygame.version.ver}')"
```

### 🔧 Fixed Issues in Latest Version:

1. **Immediate Response**: Keys now trigger immediate snake movement
2. **Better Timing**: Reduced automatic movement conflicts
3. **Focus Indicators**: Clear window title and instructions
4. **Debug Output**: Console messages show when keys are pressed

### 🎮 How the Controls Should Work:

- **WASD or Arrow Keys**: Move snake immediately
- **Direction Change**: Snake changes direction on next move
- **Invalid Moves**: Opposite direction moves are ignored (prevents suicide)
- **Timing**: Manual input overrides automatic movement timer

### 🔍 Troubleshooting Checklist:

- [ ] Game window has focus (click on it)
- [ ] Pygame version 2.5+ installed
- [ ] Virtual environment activated
- [ ] No conflicting applications capturing input
- [ ] Terminal/console shows input debug messages

### 🐍 Expected Behavior:

1. Start game with `python main.py --pygame`
2. Click on the game window
3. Press W/A/S/D - snake should move immediately
4. Console should show: "🎯 Snake moved: [DIRECTION]"

### 🆘 Still Having Issues?

Try this minimal test:
```bash
python -c "
import pygame
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption('Key Test - Press any key')
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f'Key pressed: {pygame.key.name(event.key)}')
            if event.key == pygame.K_ESCAPE:
                running = False
    clock.tick(60)
pygame.quit()
"
```

If this doesn't detect your keys, there might be a system-level issue with Pygame input handling.