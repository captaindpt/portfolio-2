# ASCII Animation Player Package

This package contains everything needed to play ASCII art animations in terminal/console environments. It's designed to be easily integrated into websites, applications, or used as a standalone component.

## 🎬 What This Does

Plays ASCII art animations with full control over playback, looping, speed, and terminal adaptation. Perfect for:
- Web applications with terminal-like interfaces
- Command-line tools and demos
- Interactive art installations
- Retro-style animations in modern apps

## 📁 Package Structure

```
ascii-animation-player/
├── src/                          # Core source code
│   ├── main.py                   # Main CLI interface (ENTRY POINT)
│   ├── player.py                 # Animation player engine
│   ├── config.py                 # Configuration system
│   ├── storage.py                # Animation file loading
│   └── terminal_utils.py         # Terminal handling utilities
├── animations/                   # Sample animation files
│   ├── d2_boat_bright1.5_contrast1.5.pkl.gz.gz
│   ├── d2_boat_braille.pkl.gz.gz
│   └── ... (multiple variations)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd ascii-animation-player
pip install -r requirements.txt
```

### 2. Play an Animation
```bash
cd src
python main.py play ../animations/d2_boat_bright1.5_contrast1.5.pkl.gz.gz --simple --loop
```

### 3. Stop with Ctrl+C

## 🎮 Usage Options

### Basic Playback
```bash
# Play once
python main.py play animation.pkl.gz.gz

# Loop forever
python main.py play animation.pkl.gz.gz --simple --loop

# Interactive mode with controls
python main.py play animation.pkl.gz.gz

# Custom speed
python main.py play animation.pkl.gz.gz --speed 2.0 --loop
```

### Available Flags
- `--simple`: Simple playback without interactive controls
- `--loop`: Loop animation indefinitely
- `--speed X.X`: Playback speed multiplier (0.5 = half speed, 2.0 = double speed)
- `--no-resize`: Disable automatic terminal resizing

### Interactive Controls (without --simple)
- `Q`: Quit
- `Space`: Pause/Resume
- `←/→`: Seek backward/forward
- `+/-`: Increase/decrease speed
- `R`: Toggle auto-resize
- `C`: Toggle centering

## 🔧 Core Components

### 1. `main.py` - The Entry Point
- Command-line interface using Click
- Handles argument parsing and validation
- Loads animations and starts playback
- **This is what you'll primarily use**

### 2. `player.py` - Animation Engine
- `ASCIIPlayer` class for playback control
- `play()` method for interactive mode
- `play_simple()` method for non-interactive mode
- Automatic terminal resizing and frame adaptation

### 3. `config.py` - Configuration System
- `ASCIIConfig` dataclass with all settings
- Playback speed, looping, terminal size handling
- Brightness, contrast, and character set options

### 4. `storage.py` - File Loading
- `ASCIIStorage` class handles compressed pickle files
- Supports `.pkl.gz.gz`, `.pkl.gz`, and uncompressed formats
- Automatic format detection

### 5. `terminal_utils.py` - Terminal Handling
- Terminal size detection
- Frame resizing and centering
- Cross-platform terminal control

## 🌐 Web Integration

### For Web Applications

#### Option 1: Server-Side Rendering
```python
# In your web app
import sys
sys.path.append('path/to/ascii-animation-player/src')

from storage import ASCIIStorage
from config import ASCIIConfig

# Load animation frames
config = ASCIIConfig()
storage = ASCIIStorage(config)
data = storage.load('animations/sample.pkl.gz.gz')
frames = data['frames']

# Send frames to frontend via WebSocket/AJAX
# Frontend can display them with JavaScript timing
```

#### Option 2: Terminal Emulator in Browser
- Use libraries like `xterm.js` or `terminal.js`
- Stream the output from the Python player
- Run the player in a subprocess and capture output

#### Option 3: Convert to Web Format
```python
# Extract frames for web use
data = storage.load('animation.pkl.gz.gz')
frames = data['frames']
fps = data['metadata']['fps']

# Convert to JSON for frontend
import json
web_data = {
    'frames': frames,
    'fps': fps,
    'frame_delay': 1000 / fps  # milliseconds
}
with open('animation.json', 'w') as f:
    json.dump(web_data, f)
```

## 📊 Animation File Format

Animation files are compressed pickle files containing:

```python
{
    'frames': [                    # List of ASCII art strings
        "ASCII frame 1...",
        "ASCII frame 2...",
        # ...
    ],
    'config': {                    # Original conversion settings
        'width': 80,
        'height': 40,
        'target_fps': 30,
        'brightness': 1.5,
        'contrast': 1.5,
        # ...
    },
    'metadata': {                  # Animation metadata
        'frame_count': 262,
        'fps': 30,
        'dimensions': [80, 40]
    },
    'version': '1.0'
}
```

## 🎨 Sample Animations Included

The package includes several animation variations:

- `d2_boat_default.pkl.gz.gz` - Standard settings
- `d2_boat_braille.pkl.gz.gz` - High-detail Braille characters
- `d2_boat_bright1.5_contrast1.5.pkl.gz.gz` - Enhanced brightness/contrast
- `d2_boat_edge_dither.pkl.gz.gz` - Artistic edge detection
- `d2_boat_highres120x60_*.pkl.gz.gz` - Higher resolution variants

## 🔄 Integration Examples

### Simple Python Integration
```python
import sys
sys.path.append('src')
from storage import ASCIIStorage
from player import ASCIIPlayer
from config import ASCIIConfig

# Load and play
storage = ASCIIStorage(ASCIIConfig())
data = storage.load('animations/sample.pkl.gz.gz')
player = ASCIIPlayer(ASCIIConfig(loop=True))
player.play_simple(data['frames'], data['metadata']['fps'])
```

### Flask Web App Example
```python
from flask import Flask, render_template
import subprocess
import threading

app = Flask(__name__)

@app.route('/play/<animation>')
def play_animation(animation):
    # Start player in background
    subprocess.Popen([
        'python', 'src/main.py', 'play', 
        f'animations/{animation}', '--simple', '--loop'
    ])
    return "Animation started!"
```

## ⚡ Performance Notes

- Animations auto-resize to fit terminal
- Higher resolution animations (120x60) use more CPU
- Braille character animations provide best detail
- Simple mode is more efficient than interactive mode
- Gzip compression reduces file size significantly

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**: Ensure you're in the `src/` directory or add it to Python path
2. **Animation not loading**: Check file path and ensure `.pkl.gz.gz` extension
3. **Garbled output**: Terminal might not support Unicode (Braille animations)
4. **Performance issues**: Try lower resolution animations or reduce playback speed

### Dependencies
All required packages are in `requirements.txt`:
- `click` - Command line interface
- `colorama` - Cross-platform terminal colors
- `numpy` - Numerical operations
- `opencv-python` - Image processing
- `Pillow` - Image manipulation
- `ascii-magic` - ASCII conversion
- `tqdm` - Progress bars

## 🎯 Perfect for:

- **Terminal-based web apps** (like VS Code's integrated terminal)
- **Command-line tools** that need visual flair
- **Retro gaming interfaces**
- **ASCII art galleries**
- **Interactive demos and presentations**
- **Background animations in terminal applications**

## 💡 Key Features

- ✅ **Automatic terminal resizing** - Works on any screen size
- ✅ **Multiple playback modes** - Simple and interactive
- ✅ **Looping support** - Perfect for background animations
- ✅ **Speed control** - Slow motion to fast forward
- ✅ **Cross-platform** - Works on Linux, macOS, Windows
- ✅ **Lightweight** - Minimal dependencies
- ✅ **Easy integration** - Import as modules or use CLI

Ready to bring ASCII art to life! 🎬 