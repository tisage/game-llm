# Snake Game Frontend Resources

This directory contains frontend-related resources and alternative implementations.

## Structure

- `static/` - Static assets (images, styles, etc.)
- `templates/` - HTML templates (if needed for custom web interface)
- `docs/` - Frontend documentation

## Current Implementation

The main frontend is implemented using **Gradio** which provides:
- Web-based interface
- Automatic UI generation
- Built-in styling and components
- Easy deployment

## Usage

To run the web frontend:
```bash
# Basic Gradio interface
python main.py --gradio

# Custom port
python main.py --gradio --port 8080

# Public sharing
python main.py --gradio --share
```

## Features

- **Interactive Controls**: Click buttons to move snake
- **Real-time Display**: Game state rendered as images
- **Responsive Design**: Works on desktop and mobile
- **Game Statistics**: Score tracking and high scores
- **Visual Feedback**: Status messages and overlays