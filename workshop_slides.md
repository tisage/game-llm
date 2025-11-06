# Vibe Coding: From Prompt to Play

**A Workshop on Rapid Game Prototyping with AI**

---

## What is "Vibe Coding"?

-   **Speaker Script:** "Welcome, everyone! Today, we're going to talk about a fun and powerful way to create software called 'Vibe Coding.'"

-   It's a development style focused on **rapid iteration** and getting a feel for the end product as quickly as possible.

-   You act as the **creative director**, guiding an AI assistant (like Gemini) to do the heavy lifting.

-   The goal isn't perfect code on the first try. It's about getting a **functional prototype** up and running, then refining it.

-   It's about capturing the "vibe" of your idea in code.

---

## The Art of the Prompt

-   **Speaker Script:** "The most critical skill in vibe coding is communication. You need to tell your AI assistant exactly what you want. This is the art of the prompt."

-   Think of yourself as a **Project Manager** and the AI as your **Developer**.

-   **Good prompts are:**
    -   **Clear:** No ambiguity.
    -   **Specific:** Provide details (like colors, sizes, and numbers).
    -   **Structured:** Organize your thoughts into logical sections.

-   A great prompt is like a great recipe. It ensures you get the result you expect.

---

## Let's Design a Game: Classic Snake

-   **Speaker Script:** "To put this into practice, we're going to design a complete game by writing a single, detailed prompt. Our example will be the classic Snake game."

-   We will break down our game design into five clear sections, just like a real design document.

-   This process will become the blueprint for our AI to follow.

---

## Step 1: The Objective

-   **Speaker Script:** "First, we need a high-level goal. What are we building? This is the objective."

-   It's a simple, one-sentence summary of the project.

-   **Our Objective:**
    > Create a complete, single-file Python application for a classic Snake game using the Pygame library. The game should be easy to run and control, featuring a clean and visually appealing interface.

---

## Step 2: Core Gameplay Mechanics

-   **Speaker Script:** "This is the most important part. We need to define the rules of our game. How does it work?"

-   **Game Board:** The play area. (e.g., 800x600 window, 20x20 grid)
-   **The Player (Snake):** How does the player move and interact? (e.g., Starts in center, controlled by WASD, can't reverse).
-   **The Goal (Food):** What does the player try to achieve? (e.g., Randomly appearing food, snake grows when it eats).
-   **Rules (Scoring & Game Over):** How do you win or lose? (e.g., +10 points per food, game ends on collision).
-   **Game Flow:** How does the game state change? (e.g., Restart with 'R' key).

---

## Step 3: GUI Design

-   **Speaker Script:** "Next, let's think about the visuals. How should our game look and feel?"

-   **Graphics & Art Style:** Define the aesthetic. Simple and clean is a great starting point. (e.g., Green snake, red food, black background).

-   **User Interface (UI):** What information does the player need? (e.g., Display the score in the top-left corner).

-   **Sound:** Don't forget audio! For our example, we'll keep it simple. (e.g., No sound effects).

---

## Step 4: The Implementation Plan

-   **Speaker Script:** "Here, we give technical instructions to our AI developer. We're telling it *how* to build the game."

-   **Language and Library:** Be explicit. (e.g., Use Python 3 and the `pygame` library).

-   **Code Structure:** This is key for good software engineering. We can ask the AI to follow best practices.
    -   Use a `class` to organize the code.
    -   Use `constants` for game parameters.
    -   Use separate methods for input, updates, and drawing.

---

## Step 5: The Deliverable

-   **Speaker Script:** "Finally, what do we want at the end? We need to define the final output."

-   For a simple game, a single file is often best.

-   **Our Deliverable:**
    > A single Python file (`snake_game.py`) containing the complete, runnable game.

---

## The Final Prompt

-   **Speaker Script:** "Now, let's put it all together. This is the prompt we would give to our AI assistant."

```markdown
# Prompt for Generating a Snake Game

## 1. Objective
Create a complete, single-file Python application for a classic Snake game...

## 2. Core Gameplay Mechanics
- **Game Board:** 800x600 window...
- **Snake:** Starts in the center...
...

## 3. GUI
- **Graphics:** Simple, clean 2D graphics...
...

## 4. Code Structure
- **Language:** Python 3, Pygame...
...

## 5. Deliverable
- A single Python file (`snake_game.py`).
```
*(You would show the full prompt text here)*

---

## Vibe Coding: Live Demo!

-   **Speaker Script:** "Now, let's see it in action. I'm going to take this prompt and use it with an AI command-line tool to generate our game from scratch."

-   **(This is where you would run the prompt through the Gemini CLI or other tool).**

-   We'll then iterate on it, maybe adding a new feature like a pause button or a new visual style.

---

## Recap & Your Turn

-   **Recap the process:**
    1.  **Idea:** We had an idea for a game.
    2.  **Prompt:** We translated that idea into a detailed, structured design document.
    3.  **Code:** The AI generated the code based on our blueprint.
    4.  **Refine:** We can easily tweak the design and have the AI apply the changes.

-   **Your Turn:** Use the `game_design_template.md` to design your own simple game!

-   **Q & A**
