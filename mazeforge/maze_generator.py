from typing import List, Union, Tuple, Literal
from PIL import Image

def generate_maze(
    width: int = 10, 
    height: int = 10,
    name: str = "GeneratedMaze",
    algorithm: Literal["simple", "growing_tree", "braided"] = "growing_tree",
    algorithm_settings: dict = None,
    mode: Literal["list", "image", "distances", "dict"] = "list",
    image_settings: dict = None,
    seed: int = None,
    start_wall: Literal["N", "S", "E", "W", "Any"] = "Any",
    end_wall: Literal["N", "S", "E", "W", "Any"] = "Any"
) -> Union[List[List[str]], Image.Image, List[List[Union[dict, str]]]]:
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
                'weighHigh': 0-100 (default 99),
                'weightLow': 0-100 (default 97)
            }
            braided: {
                'weightBraid': -1 to 100 (default -1)
                    -1: removes all dead ends
                    0-100: percentage chance of creating loops
            }
        mode: Output mode (default: "list")
            - "list": Returns maze as nested list
            - "dict": Returns maze as nested list with cell dictionaries
            - "image": Returns PIL Image object
            - "distances": Returns maze with distances from start
        image_settings: Dict with image settings:
            {
                'mode': '1' or 'RGB' (default: 'RGB'),
                'wall_color': color value (default: 'Black'),
                'floor_color': color value (default: 'White'),
                'pixel_size': int (default: 10)
            }
        start_wall: Which wall to place start point on (default: "Any")
            - "N": North wall
            - "S": South wall
            - "E": East wall
            - "W": West wall
            - "Any": Random wall
        end_wall: Which wall to place end point on (default: "Any")
            - "N": North wall
            - "S": South wall
            - "E": East wall
            - "W": West wall
            - "Any": Random wall
    
    Returns:
        List[List[str]] if mode="list": 
            '#' = wall
            ' ' = path
            'S' = start
            'E' = end
        List[List[Union[dict, str]]] if mode="dict":
            '#' = wall
            dict = {
                "distance": steps from start (-1 if unreachable),
                "index": str (' ' for path, '#' for wall, 'S' for start, 'E' for end),
                "N": bool (has north connection),
                "S": bool (has south connection),
                "W": bool (has west connection),
                "E": bool (has east connection)
            }
        List[List[Union[str, int]]] if mode="distances":
            '#' = wall
            int = steps from start
            'E' = end
        PIL.Image if mode="image"
    """
    from .Maze import Maze
    # Default settings
    default_algo_settings = {
        'weighHigh': 99,
        'weightLow': 97,
        'weightBraid': -1
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
    maze = Maze(width, height, mazeName=name, seed=seed)
    maze.start_wall = start_wall
    maze.end_wall = end_wall
    
    # Apply selected algorithm
    if algorithm == "simple":
        maze.makeMazeSimple()
    elif algorithm == "growing_tree":
        maze.makeMazeGrowTree(
            weightHigh=default_algo_settings['weighHigh'],
            weightLow=default_algo_settings['weightLow']
        )
    elif algorithm == "braided":
        maze.makeMazeGrowTree(
            weightHigh=default_algo_settings['weighHigh'],
            weightLow=default_algo_settings['weightLow']
        )
        maze.makeMazeBraided(default_algo_settings['weightBraid'])
    
    # Return based on mode
    if mode == 'list':
        return maze.get_maze_as_list()
    elif mode == 'dict':
        return maze.get_maze_detailed_info()
    elif mode == 'distances':
        return maze.get_maze_with_distances()
    else:
        image = maze.makePP(
            mode=default_image_settings['mode'],
            colorWall=default_image_settings['wall_color'],
            colorFloor=default_image_settings['floor_color'],
            pixelSizeOfTile=default_image_settings['pixel_size']
        )
        return image 