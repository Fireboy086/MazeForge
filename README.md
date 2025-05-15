# MazeForge 🌟

A flexible and powerful maze generation library with multiple algorithms and customization options.

## Requirements ⚙️

- Python 3.6 or higher
- Pillow (PIL) library for image generation

## Credits 👏

This project is based on the maze generation code originally written by [turidus](https://github.com/turidus) and modified with additional features. The core maze generation algorithms were inspired by their work.

## Features 🎮

- **Multiple Algorithms**:
  - Simple (Prim's algorithm)
  - Growing Tree (customizable weights)
  - Braided (with loop generation)
- **Smart Entry/Exit Points**: Automatically places start and end points far apart (30% of maze size)
- **Multiple Output Formats**:
  - Text-based (nested list)
  - Image (PIL Image object)
- **Highly Customizable**:
  - Maze size
  - Algorithm parameters
  - Colors and pixel size
  - Entry/exit point distance

## Installation 📦

```bash
pip install mazeforge
```

## Quick Start 🚀

```python
from mazeforge import generate_maze

# Text maze (walls: '#', paths: ' ')
maze = generate_maze(10, 10)
for row in maze:
    print(''.join(row))

# Colorful image maze
maze_img = generate_maze(
    20, 20,
    algorithm="braided",
    mode="image",
    image_settings={
        'wall_color': 'Yellow',
        'floor_color': 'Red'
    }
)
maze_img.save('maze.png')
```

## Advanced Usage 🛠️

### Different Algorithms

```python
# Prim's algorithm
maze = generate_maze(algorithm="simple")

# Growing Tree with custom weights
maze = generate_maze(
    algorithm="growing_tree",
    algorithm_settings={
        'weight_high': 100,  # 0-100
        'weight_low': 95     # 0-100
    }
)

# Braided maze with loops
maze = generate_maze(
    algorithm="braided",
    algorithm_settings={
        'weight_braid': 30  # -1: remove dead ends
                           # 0-100: % chance of loops
    }
)
```

### Image Customization

```python
maze_img = generate_maze(
    width=30,
    height=30,
    mode="image",
    image_settings={
        'mode': 'RGB',           # '1' or 'RGB'
        'wall_color': 'White',   # color name or RGB tuple
        'floor_color': 'Black',  # color name or RGB tuple
        'pixel_size': 20         # size of each cell
    }
)
```

## API Reference 📚

### generate_maze()

```python
def generate_maze(
    width: int = 10,
    height: int = 10,
    name: str = "GeneratedMaze",
    algorithm: str = "growing_tree",
    algorithm_settings: dict = None,
    mode: str = "list",
    image_settings: dict = None
) -> Union[List[List[str]], Image.Image]
```

Parameters:
- `width`, `height`: Maze dimensions
- `name`: Optional name for the maze
- `algorithm`: "simple", "growing_tree", or "braided"
- `algorithm_settings`: Dictionary of algorithm-specific settings
- `mode`: "list" or "image"
- `image_settings`: Dictionary of image generation settings

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 