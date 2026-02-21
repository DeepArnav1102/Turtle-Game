# 🐢 Turtle Game

A Python-based interactive turtle drawing app built with `turtle`, `tkinter`, and `Pillow`. Control a turtle on a canvas, draw freely, fill shapes, erase, and fully customize colors — all from your keyboard.

---

## ✨ Features

- 🎨 **Custom colors** — choose your own background color, pen color, and fill color at startup
- ✏️ **Drawing modes** — draw freely, lift the pen, or switch to eraser mode
- 🪣 **Fill mode** — enclose a shape and fill it with your chosen fill color
- ⚡ **Speed control** — adjust turtle speed from 1 (slow) to 5 (fast)
- 📏 **Pen width control** — adjust pen thickness from 1 to 5
- 🔄 **Continuous mode** — let the turtle keep moving forward automatically
- 🚧 **Boundary detection** — the turtle cannot move outside the canvas area
- 👁️ **Show/Hide turtle** — toggle turtle visibility while drawing

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pillow library

Install Pillow with:

```bash
pip install Pillow
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DeepArnav1102/Turtle-Game.git
   cd Turtle-Game
   ```

2. **Ensure `TurtleBG.png` is in the same folder as `turtl1e.py`.**

3. **Run the game:**

   ```bash
   python turtl1e.py
   ```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Turn left (30°) |
| `D` | Turn right (30°) |
| `Q` | Toggle pen up / pen down |
| `E` | Toggle continuous forward movement |
| `Z` | Toggle eraser mode |
| `F` | Toggle fill mode (press again to fill the shape) |
| `C` | Clear the canvas |
| `U` | Increase pen width |
| `J` | Decrease pen width |
| `V` | Show / hide the turtle |
| `↑` | Increase speed |
| `↓` | Decrease speed |
| `M` | Exit the game |

---

## 🖥️ How It Works

1. **Start Screen** — A splash screen with the game title and a Start button is displayed over the background image.
2. **Background Color** — Enter a valid tkinter color name (e.g. `lightblue`, `black`) for the canvas background.
3. **Pen & Fill Color** — Enter colors for the pen stroke and shape fill.
4. **Canvas** — The turtle canvas (1000×700) opens alongside an on-screen instructions panel. Use the keyboard controls to draw!

> ⚠️ If an invalid color name is entered, the app falls back to defaults (white background, black pen).

---

## 📁 Project Structure

```
Turtle-Game/
├── turtl1e.py      # Main application script
└── TurtleBG.png    # Background image for the start screen
```

---

## 🛠️ Built With

- [Python](https://www.python.org/) — Core language
- [Turtle](https://docs.python.org/3/library/turtle.html) — Drawing and movement
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI and window management
- [Pillow](https://python-pillow.org/) — Background image loading

---

## 📄 License

This project is open source. Feel free to fork, modify, and build upon it!
