#!/bin/bash
# Workshop Cleanup Script

echo "🧹 Cleaning up workshop demo files..."

# Remove any demo directories created during workshop
if [ -d "snake-demo" ]; then
    echo "Removing snake-demo directory..."
    rm -rf snake-demo
fi

# Clean up any temporary files
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

# Clean up any AI-generated files that might be in the wrong location
if [ -f "snake_game.py" ]; then
    echo "Moving snake_game.py to demo-results/ for archival..."
    mkdir -p demo-results
    mv snake_game.py demo-results/
fi

echo "✅ Cleanup complete!"
echo ""
echo "📁 Your workshop materials are preserved in:"
echo "   - docs/workshop_prompts_optimized.md"
echo "   - docs/demo_script.md" 
echo "   - backup_snake_game.py"
echo ""
echo "🗂️  Any demo results are saved in demo-results/"