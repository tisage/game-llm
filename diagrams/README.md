# Mermaid Diagrams for Workshop Slides

This folder contains mermaid diagram source files that are referenced in the workshop slides.

## Diagrams

1. **vibe-coding-workflow.md** - Shows the overall vibe coding process from idea to finished game
2. **prompt-structure.md** - Breaks down the 5-section prompt framework
3. **development-iteration-cycle.md** - Illustrates the iterative improvement process
4. **game-development-process.md** - Complete flowchart for workshop participants
5. **ai-tool-selection.md** - Shows the two recommended AI CLI tools for students (GitHub Copilot CLI and Gemini CLI)

## How to Render

You need to render these mermaid diagrams to PNG images and save them in a `pic/` folder at the root of the project.

### Option 1: Using Mermaid CLI

```bash
# Install mermaid-cli globally
npm install -g @mermaid-js/mermaid-cli

# Render all diagrams
mmdc -i diagrams/vibe-coding-workflow.md -o pic/vibe-coding-workflow.png
mmdc -i diagrams/prompt-structure.md -o pic/prompt-structure.png
mmdc -i diagrams/development-iteration-cycle.md -o pic/development-iteration-cycle.png
mmdc -i diagrams/game-development-process.md -o pic/game-development-process.png
mmdc -i diagrams/ai-tool-selection.md -o pic/ai-tool-selection.png
```

### Option 2: Using Online Tools

1. Visit [Mermaid Live Editor](https://mermaid.live/)
2. Copy the mermaid code from each `.md` file
3. Export as PNG
4. Save to `pic/` folder with the corresponding filename

### Option 3: Using VS Code Extension

1. Install the "Markdown Preview Mermaid Support" extension
2. Open each diagram file
3. Right-click on the diagram in preview
4. Select "Save as PNG"
5. Save to `pic/` folder

## Expected Output Structure

```
game-llm/
├── diagrams/           (mermaid source files - this folder)
│   ├── vibe-coding-workflow.md
│   ├── prompt-structure.md
│   ├── development-iteration-cycle.md
│   ├── game-development-process.md
│   └── ai-tool-selection.md
└── pic/               (rendered PNG images)
    ├── vibe-coding-workflow.png
    ├── prompt-structure.png
    ├── development-iteration-cycle.png
    ├── game-development-process.png
    └── ai-tool-selection.png
```

## References in Workshop Slides

These diagrams are already referenced in `workshop_slides.md` with the paths:
- `./pic/vibe-coding-workflow.png`
- `./pic/prompt-structure.png`
- `./pic/ai-tool-selection.png`
- `./pic/development-iteration-cycle.png`
- `./pic/game-development-process.png`
