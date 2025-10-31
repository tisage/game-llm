# 🐍 Snake Game - Complete Implementation

A fully functional Snake game implementation with both desktop (Pygame) and web (Gradio) interfaces, built using AI-assisted development techniques.

## 🎯 Project Overview

This project implements the classic Snake game with modern Python technologies, demonstrating AI-powered development workflows:

### Backend (`src/game_core/`)
- **Pure Python game logic** - No UI dependencies
- **Modular architecture** - Separate components for different game aspects
- **Comprehensive state management** - Complete game state tracking
- **Collision detection** - Wall and self-collision algorithms
- **Scoring system** - Score tracking with high score persistence

### Frontend Options

#### 1. Pygame Desktop Interface (`src/pygame_ui/`)
- **Real-time gameplay** - Smooth WASD/Arrow key controls
- **60 FPS rendering** - Fluid visual experience
- **Rich graphics** - Enhanced snake and food visuals
- **Immediate feedback** - Instant response to input

#### 2. Gradio Web Interface (`src/gradio_ui/`)
- **Web-based interface** - Accessible from any browser
- **Turn-based gameplay** - Click buttons to move
- **Modern UI** - Clean, responsive design
- **Easy sharing** - Public links available

## 🚀 Quick Start

### Installation
```bash
# Setup virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Game

#### Pygame Version (Recommended for gameplay)
```bash
python main.py --pygame
```
**Controls:**
- W/A/S/D or Arrow Keys - Move snake
- R - Restart game
- P/Space - Pause/Resume
- ESC - Quit

#### Gradio Web Version (Great for sharing)
```bash
python main.py --gradio
```
Opens web interface at http://localhost:7860

#### Both Versions Simultaneously
```bash
python main.py --both
```

### Advanced Options
```bash
# Custom port for web interface
python main.py --gradio --port 8080

# Public sharing link
python main.py --gradio --share

# Help and options
python main.py --help
```

## 🎮 Game Features

### Core Gameplay
- **Grid-based movement** - 20×15 game grid
- **Food consumption** - Eat red food to grow and score
- **Collision detection** - Avoid walls and yourself
- **Score system** - 10 points per food item
- **High score tracking** - Persistent across sessions

### Visual Features
- **Enhanced graphics** - Snake with eyes, highlighted food
- **Real-time UI** - Score, length, and status display
- **Game overlays** - Game over and pause screens
- **Visual feedback** - Status messages and animations

### Technical Features
- **Multiple interfaces** - Desktop and web versions
- **Modular design** - Easy to extend and modify
- **Comprehensive testing** - Full test suite included
- **Error handling** - Graceful failure recovery

## 🏗️ Architecture

### Backend Structure
```
src/game_core/
├── constants.py      # Game configuration
├── snake.py          # Snake entity logic
├── food.py           # Food generation and management
├── collision.py      # Collision detection algorithms
├── scoring.py        # Score calculation and tracking
└── game_state.py     # Main game engine
```

### Frontend Structure
```
src/pygame_ui/
├── game_loop.py      # Main Pygame game loop
├── renderer.py       # Graphics rendering
└── input_handler.py  # Keyboard input processing

src/gradio_ui/
├── web_interface.py  # Main Gradio interface
├── image_renderer.py # Game state to image conversion
└── control_handler.py # Button action processing
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
# Test core functionality
python tests/test_core.py

# Test Gradio components
python tests/test_gradio.py

# Full test suite
python tests/test_complete.py
```

## 🎯 Design Principles

### 1. Separation of Concerns
- **Game logic** is independent of UI
- **Rendering** is separated from game state
- **Input handling** is modular and swappable

### 2. Modular Architecture
- Each component has a single responsibility
- Components communicate through well-defined interfaces
- Easy to add new features or UI methods

### 3. Multi-Interface Support
- Same game logic powers both interfaces
- Consistent gameplay across platforms
- Easy to add new interface types

---

## 📚 AI-Powered Development Workshop

This Snake game was built as part of the **AI-Powered Game Development Workshop**, demonstrating:

### 🤖 AI-Assisted Development
- **GitHub Copilot CLI** for rapid code generation
- **Prompt engineering** for specific game features
- **AI-guided architecture** decisions
- **Automated testing** suggestions

### 🎓 Learning Outcomes
- Modern Python development patterns
- Multi-interface application design
- Testing and quality assurance
- AI collaboration workflows

### 🔧 Development Process
1. **AI-Assisted Planning** - Architecture design with AI input
2. **Rapid Prototyping** - Core logic development
3. **Interface Implementation** - Multiple UI approaches
4. **Testing & Validation** - Comprehensive test coverage
5. **Documentation** - AI-assisted documentation generation

---

## 🛠️ Tech Stack & Prerequisites

### Required Tools
- **Python 3.9+** (with virtual environment support)
- **VS Code** with GitHub Copilot extension
- **GitHub Copilot CLI** (Pro/Education account)
- **Git** for version control

### Python Libraries
- **Gradio** - Web-based UI for Python apps
- **NumPy** - Grid and array manipulation
- **Pillow (PIL)** - Image processing for game visuals

### Knowledge Prerequisites
- Basic Python programming (variables, functions, classes)
- Basic command line usage
- Familiarity with VS Code (helpful but not required)

---

## 🚀 Workshop Setup

### 1. Environment Setup
```bash
# Clone this repository
git clone <repository-url>
cd game-llm

# Create and activate virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Copilot CLI Installation
```bash
# Check if Copilot CLI is installed
gh copilot --version

# If not installed, install it:
gh extension install github/gh-copilot
```

---

## 📋 Workshop Agenda

### Part 1: Introduction (15 min)
- AI in software development
- GitHub Copilot CLI overview
- Workshop objectives and outcomes

### Part 2: From Idea to Code (30 min)
- **Step 1**: Project planning with AI prompts
- **Step 2**: Setting up the development environment
- **Step 3**: Creating the game structure with Copilot
- **Step 4**: Implementing game logic with AI assistance

### Part 3: Enhancement & Visualization (20 min)
- **Step 5**: Adding Gradio web interface
- **Step 6**: Improving visuals and user experience
- **Step 7**: Testing and debugging

### Part 4: Reflection & Next Steps (10 min)
- Discussing AI-human collaboration
- Course preview and registration information
- Q&A session

---

## 🎯 Learning Outcomes

By the end of this workshop, participants will:

1. **Understand AI-Assisted Development**
   - Use GitHub Copilot CLI for code generation
   - Write effective prompts for programming tasks
   - Collaborate effectively with AI tools

2. **Build a Complete Game Application**
   - Create a functional Snake game from scratch
   - Implement game logic and user interface
   - Deploy a web-based application using Gradio

3. **Learn Modern Development Practices**
   - Use virtual environments for Python projects
   - Practice version control with Git
   - Follow structured development workflows

4. **Explore Career Opportunities**
   - Understand the impact of AI on software development
   - Preview advanced topics in generative AI applications
   - Connect with upcoming course offerings

---

## 📁 Project Structure

```
game-llm/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── docs/
│   ├── workshop-guide.md         # Detailed step-by-step guide
│   ├── CISC3XX S26 Syllabus.pdf  # Course information
├── src/                          # Main source code (.py files for VS Code)
│   ├── snake_game.py            # Core game logic
│   ├── game_ui.py               # Gradio interface
│   ├── main.py                  # Application entry point
│   └── utils.py                 # Helper functions and utilities
├── examples/                     # Reference implementations
│   ├── basic_snake.py           # Simple console version
│   └── advanced_snake.py        # Enhanced version with features
├── notebooks/                    # Jupyter notebooks (Colab backup)
│   ├── snake_game_workshop.ipynb # Complete workshop notebook
│   └── quick_demo.ipynb         # Quick demo for backup
├── prompts.md                    # AI prompts library and templates
└── .venv/                       # Virtual environment (created locally)
```

---

## 🎮 What We'll Build

### Snake Game Features
- **Interactive Grid**: 10x10 or 20x20 game board
- **Real-time Controls**: Arrow buttons for snake movement
- **Score System**: Points for eating food
- **Game States**: Start, playing, game over
- **Visual Feedback**: Colorful graphics and status messages
- **Web Interface**: Playable in any browser via Gradio

### Technical Highlights
- **Object-Oriented Design**: Clean, maintainable code structure
- **Real-time Updates**: Smooth game state transitions
- **Responsive UI**: Works on desktop and mobile devices
- **Modular Architecture**: Easy to extend and modify

---

## 🚦 Getting Started

Ready to begin? Choose your preferred method:

### 🖥️ VS Code Method (Recommended for Live Demo)
1. **Complete the setup** (see Workshop Setup section above)
2. **Open VS Code** and navigate to the project directory
3. **Follow along** with the instructor using `src/` files
4. **Use GitHub Copilot CLI** for real-time code generation

### 📱 Google Colab Method (Backup/Remote Access)
1. **Open Google Colab** in your browser
2. **Upload** `notebooks/snake_game_workshop.ipynb`
3. **Follow the notebook** cell by cell
4. **Share your results** with the generated public link

### 📖 Detailed Instructions
For complete step-by-step instructions, see: [`docs/workshop-guide.md`](docs/workshop-guide.md)

---

## 📖 Additional Resources

- **Workshop Guide**: Detailed step-by-step instructions
- **Prompts Library**: Collection of AI prompts used in the workshop
- **GitHub Copilot Documentation**: https://docs.github.com/en/copilot
- **Gradio Documentation**: https://gradio.app/docs/
- **Course Information**: See `docs/CISC3XX S26 Syllabus.pdf`

---

## 👨‍🏫 About the Instructor

This workshop is designed and led by a CS/AI professor with expertise in:
- Artificial Intelligence and Machine Learning
- Software Engineering and Development
- Educational Technology and Pedagogy
- Industry Applications of AI Tools

---

## 🎓 Course Information

Interested in learning more? Consider enrolling in:

**CISC 3XX — Applied Generative AI and LLM Applications**  
*Spring 2026*

This course covers:
- Advanced prompt engineering techniques
- Building LLM-powered applications
- AI ethics and responsible development
- Industry case studies and projects
- Career preparation in AI development

*Registration information available at the end of the workshop.*

---

## 🤝 Contributing & Feedback

We welcome feedback and contributions to improve this workshop:
- Submit issues or suggestions via GitHub
- Share your enhanced game versions
- Propose additional features or examples

---

## 📜 License

This educational material is provided under the MIT License. See `LICENSE` file for details.

---

**Ready to build something amazing with AI? Let's get started! 🚀**
