import random
# import random to add walls inside the maze


# Constants for maze characters
WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

def generate_maze(n, wall_percentage=25):
    
    # Generates a random maze of size n x n with walls and open spaces.

    # Parameters:
    #  n: Size of the maze.
    #  wall_percentage: Percentage of walls in the maze.

    # Returns:
    #  The generated maze as a 2D list.
    
    maze = [[OPEN_SPACE] * n for _ in range(n)]

    # Add walls
    num_walls = int((wall_percentage / 100) * (n * n))
    for _ in range(num_walls):
        
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = WALL

    # Set start and end points
    maze[0][0] = START
    maze[n - 1][n - 1] = END

    return maze

def main():

    # while loop will run till the user doesn't to exit the game.
    while True:
        n = int(input("Enter the size of the maze (n x n): "))

        # if value of "n" is Invalid.
        while n <= 1:
            print("\nInvalid input, Please enter the size of maze (n x n) > 1")
            n = int(input("\nEnter the size of the maze (n x n): "))

        # maze = generate_maze(n)
        # print("\nGenerated Maze:")
        # print_maze(maze)

main()