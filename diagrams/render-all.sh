#!/bin/bash

# Script to render all mermaid diagrams to PNG images
# Requires: npm install -g @mermaid-js/mermaid-cli

# Create pic directory if it doesn't exist
mkdir -p ../pic

# Render each diagram
echo "Rendering diagrams..."

mmdc -i vibe-coding-workflow.md -o ../pic/vibe-coding-workflow.png -b transparent
echo "✓ vibe-coding-workflow.png"

mmdc -i prompt-structure.md -o ../pic/prompt-structure.png -b transparent
echo "✓ prompt-structure.png"

mmdc -i development-iteration-cycle.md -o ../pic/development-iteration-cycle.png -b transparent
echo "✓ development-iteration-cycle.png"

mmdc -i game-development-process.md -o ../pic/game-development-process.png -b transparent
echo "✓ game-development-process.png"

mmdc -i ai-tool-selection.md -o ../pic/ai-tool-selection.png -b transparent
echo "✓ ai-tool-selection.png"

echo ""
echo "All diagrams rendered successfully to ../pic/ folder!"
echo "You can now view them in your workshop slides."
