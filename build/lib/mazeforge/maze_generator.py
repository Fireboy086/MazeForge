from typing import List, Union, Tuple, Literal
from PIL import Image

def generate_maze(
    width: int = 10, 
    height: int = 10,
    name: str = "GeneratedMaze",
    algorithm: Literal["simple", "growing_tree", "braided"] = "growing_tree",
    algorithm_settings: dict = None,
    mode: Literal["list", "image"] = "list",
    image_settings: dict = None
) -> Union[List[List[str]], Image.Image]:
    """
    Generate a maze with all available settings
    
    Args:
        width: Width of maze (default: 10)
        height: Height of maze (default: 10)
        name: Name of the maze (default: "GeneratedMaze")
        algorithm: Which algorithm to use (default: "growing_tree")
            - "simple": Uses Prim's algorithm
            - "growing_tree": Uses Growing Tree algorithm
            - "braided": Uses Growing Tree + braiding for loops
        algorithm_settings: Dict with algorithm settings:
            growing_tree: {
                'weight_high': 0-100 (default 99),
                'weight_low': 0-100 (default 97)
            }
            braided: {
                'weight_braid': -1 to 100 (default -1)
                    -1: removes all dead ends
                    0-100: percentage chance of creating loops
            }
        mode: Output mode (default: "list")
            - "list": Returns maze as nested list
            - "image": Returns PIL Image object
        image_settings: Dict with image settings:
            {
                'mode': '1' or 'RGB' (default: 'RGB'),
                'wall_color': color value (default: 'Black'),
                'floor_color': color value (default: 'White'),
                'pixel_size': int (default: 10)
            }
    
    Returns:
        List[List[str]] if mode="list": 
            '#' = wall
            ' ' = path
            'S' = start
            'E' = end
        PIL.Image if mode="image"
    
    Example:
        >>> # Simple list maze
        >>> maze = generate_maze(10, 10)
        >>> 
        >>> # Colored image maze with loops
        >>> maze_img = generate_maze(
        ...     width=20, 
        ...     height=20,
        ...     algorithm="braided",
        ...     algorithm_settings={'weight_braid': 30},
        ...     mode="image",
        ...     image_settings={
        ...         'wall_color': 'Yellow',
        ...         'floor_color': 'Red'
        ...     }
        ... )
    """
    from .Maze import Maze
    
    # Default settings
    default_algo_settings = {
        'weight_high': 99,
        'weight_low': 97,
        'weight_braid': -1
    }
    
    default_image_settings = {
        'mode': 'RGB',
        'wall_color': 'Black',
        'floor_color': 'White',
        'pixel_size': 10
    }
    
    if algorithm_settings:
        default_algo_settings.update(algorithm_settings)
    if image_settings:
        default_image_settings.update(image_settings)
    
    # Create maze
    maze = Maze(width, height, mazeName=name)
    
    # Apply selected algorithm
    if algorithm == "simple":
        maze.makeMazeSimple()
    elif algorithm == "growing_tree":
        maze.makeMazeGrowTree(
            weightHigh=default_algo_settings['weight_high'],
            weightLow=default_algo_settings['weight_low']
        )
    elif algorithm == "braided":
        maze.makeMazeGrowTree(
            weightHigh=default_algo_settings['weight_high'],
            weightLow=default_algo_settings['weight_low']
        )
        maze.makeMazeBraided(default_algo_settings['weight_braid'])
    
    # Return based on mode
    if mode == 'list':
        return maze.get_maze_as_list()
    else:
        image = maze.makePP(
            mode=default_image_settings['mode'],
            colorWall=default_image_settings['wall_color'],
            colorFloor=default_image_settings['floor_color'],
            pixelSizeOfTile=default_image_settings['pixel_size']
        )
        return image 