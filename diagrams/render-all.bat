@echo off
REM Script to render all mermaid diagrams to PNG images
REM Requires: npm install -g @mermaid-js/mermaid-cli

REM Create pic directory if it doesn't exist
if not exist "..\pic" mkdir "..\pic"

REM Render each diagram
echo Rendering diagrams...

call mmdc -i vibe-coding-workflow.md -o ..\pic\vibe-coding-workflow.png -b transparent
echo + vibe-coding-workflow.png

call mmdc -i prompt-structure.md -o ..\pic\prompt-structure.png -b transparent
echo + prompt-structure.png

call mmdc -i development-iteration-cycle.md -o ..\pic\development-iteration-cycle.png -b transparent
echo + development-iteration-cycle.png

call mmdc -i game-development-process.md -o ..\pic\game-development-process.png -b transparent
echo + game-development-process.png

call mmdc -i ai-tool-selection.md -o ..\pic\ai-tool-selection.png -b transparent
echo + ai-tool-selection.png

echo.
echo All diagrams rendered successfully to ..\pic\ folder!
echo You can now view them in your workshop slides.
pause
