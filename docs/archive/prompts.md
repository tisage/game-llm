
---

## 💬 **PROMPT.md**

This file guides your students (and workshop participants) through how the idea was turned into working code — from conceptual prompts to Copilot/Claude commands.

```markdown
# 🧠 Prompt Journey: From Idea to Playable Snake Game

This document shows how we used **Prompt Engineering + Copilot CLI + Python + Gradio**  
to go from a simple idea → AI-generated code → playable web app.

---

## 🪄 Step 1. Concept Prompt — Idea Generation
Ask Copilot or Claude:
> "I want to build a simple browser-based Snake game using Python and Gradio.  
> It should show a 10x10 grid, let players control the snake using arrow buttons,  
> display the score, and show 'Game Over' when the snake hits the wall or itself."

*(Goal: generate high-level structure — class for game state, rendering logic, and Gradio interface.)*

---

## ⚙️ Step 2. Design Prompt — Structure Planning
> "Design the architecture for this Snake game:  
> - One class `SnakeGame` with methods: `reset()`, `step(action)`, and `render()`  
> - Use a numpy array for the grid and RGB values for color  
> - Use Gradio Blocks for visualization and arrow buttons for control"

*(Goal: let Copilot outline the class structure and helper functions.)*

---

## 💻 Step 3. Implementation Prompt — Code Generation
> "Now implement the Python code for the SnakeGame class and the Gradio interface.  
> The interface should have arrow buttons and update the image and score in real time."

*(Goal: get working code that runs directly in VS Code or Colab.)*

---

## 🎨 Step 4. Enhancement Prompt — Make It Fun
> "Add a score counter, colorful visuals (green snake, red food),  
> and a message text area that shows '💥 Game Over!' when the player loses."

*(Goal: improve UX and engagement.)*

---

## 🧩 Step 5. Reflection Prompt — Learning Discussion
> "Explain how this workflow demonstrates AI-assisted programming.  
> What parts were human-designed, and what parts were AI-generated?"

*(Goal: encourage discussion about collaboration between human creativity and AI coding.)*

---

## 🧰 Bonus Prompts (for exploration)
- “Make the grid size adjustable (10x10, 20x20).”
- “Add a restart button in Gradio.”
- “Add sound effects or animations.”
- “Convert this Snake game into a two-player version.”

---

## ✅ Summary
This demo highlights:
- How AI tools like **Copilot CLI** and **Claude** can generate code from structured prompts.
- How **Gradio** enables instant visualization of Python apps.
- How **Prompt Engineering** transforms ideas into real projects — fast.

> 💡 *Future of coding: Talk to your IDE, not just type into it.*
```

---

it seems that you are trying to make this demo with full-code. but all I need is that you prepare the prompts_details.md for me so that I can enter these promtps step-by-step in my copilot cli or any other ai command-line tools so that it will discuss the game design with me and generate the code step-by-step, even including debuging. and then it will show me the final code and run the game in gradio localhost.

---

# 🎯 Step-by-Step AI Prompts for Live Snake Game Development

**Workshop Format**: Interactive AI-assisted coding with GitHub Copilot CLI  
**Goal**: Build a working Snake game from scratch using AI prompts  
**Duration**: 20-30 minutes of live coding  
**Technology**: Pygame for real-time controls and simple graphics  
**Files to create**: `snake_game.py` (complete playable game)

## Prompts

```bash
I want to build a Snake game using Python, Pygame and Gradio. It should have keyboard controls, real-time movement, and simple graphics. What should be the main components and architecture?"

For the Pygame Snake game, I need: use AWSD key controls, 20x15 grid, real-time movement, collision detection, food consumption, and score display on Gradio. How to begin with?

Don't show me code for now. I need to discuss the design, framework, and architecture first.

```

## Design and start implementation

```bash
I'm using `.venv` for virtual environment. so you may need to provide all necessary setup for the packages requires. like `requirements.txt` file.

next, your logic looks good. so can you start the code implmentation for the backend code in `src` folder and frontend code in `frotend` folder? you will also test your code after every major implementation.

```

## Test and Debugging

```bash
why when I enter my awsd keys the snake is not moving? can you help me debug this issue?

```

## Imprevements

```bash

```