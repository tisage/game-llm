# 🎮 AI-Powered Game Development Workshop

Welcome to the **AI-Powered Game Development Workshop**! This hands-on session demonstrates how modern AI tools like **GitHub Copilot CLI**, **VS Code**, and **Python** can transform your ideas into playable games in minutes, not hours.

> 🎯 **Workshop Goal**: Build a complete Snake game from scratch using AI-assisted coding, showcasing the power of prompt engineering and AI collaboration in software development.

---

## 📚 About This Workshop

This workshop is designed for students interested in:
- **AI-Assisted Programming** with GitHub Copilot CLI
- **Rapid Prototyping** with Python and Gradio
- **Modern Development Workflows** using VS Code and Git
- **The Future of Software Development** with AI tools

### 🎓 Course Connection
This workshop provides a preview of techniques and tools covered in:
**CISC 3XX — Applied Generative AI and LLM Applications** (Spring 2026)

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
