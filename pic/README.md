# Workshop Slide Diagrams

This folder contains rendered PNG images of all mermaid diagrams used in the workshop slides.

## Files

| Filename | Description | Used in Slide |
|----------|-------------|---------------|
| `vibe-coding-workflow.png` | Overall vibe coding process from idea to finished game | "What is Vibe Coding?" |
| `prompt-structure.png` | 5-section prompt framework breakdown | "Let's Design a Game: Classic Snake" |
| `ai-tool-selection.png` | Decision tree for choosing the right AI CLI tool | "Vibe Coding: Live Demo!" |
| `development-iteration-cycle.png` | Iterative improvement process | "Vibe Coding: Live Demo!" |
| `game-development-process.png` | Complete flowchart for workshop participants | "Recap & Your Turn" |

## Source Files

All diagrams are generated from mermaid source files located in the `../diagrams/` folder.

To regenerate these images, run:
```bash
cd ../diagrams
./render-all.sh  # On Mac/Linux
# or
render-all.bat   # On Windows
```

## Diagram Details

### 1. Vibe Coding Workflow (17 KB)
Shows the circular process: Idea → Prompt → AI Tool → Code → Test → Refine

### 2. Prompt Structure (20 KB)
Hierarchical breakdown of the 5 sections:
- Objective
- Core Gameplay Mechanics
- GUI Design
- Implementation Plan
- Deliverable

### 3. AI Tool Selection
Shows the two recommended AI CLI tools for this workshop:
- GitHub Copilot CLI (FREE for students with GitHub Education)
- Gemini CLI (FREE tier for everyone)

### 4. Development Iteration Cycle (58 KB)
Shows the feedback loop for improving generated games:
Test → Identify Issues → Update Prompt → AI Tool → Updated Code → Test

### 5. Game Development Process (121 KB)
Complete workshop workflow:
- Choose example or create own
- Use template
- Run AI CLI
- Install dependencies
- Test and iterate
- Share creation
