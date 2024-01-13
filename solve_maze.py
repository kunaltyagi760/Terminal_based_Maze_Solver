import random
# import random to add walls inside the maze.


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

def print_maze(maze):
    
    # Prints the maze in the terminal.

    # Parameters:
    #  maze: The maze to be printed.
    
    for row in maze:

        # colored_str string is printed before and after every row of maze to enhance maze representation in terminal alse maze cell is clearly visible.

        colored_str = (('\033[91m' + "+---" + '\033[0m') * len(maze)) + '\033[91m' + "+" + '\033[0m'
        print(colored_str)
        for cell in row:
            print("|", end=" ")
            print(cell, end=" ")
        print("|", end=" ")
        print()
    print(colored_str)

def find_path(maze, cur_row, cur_col, size):
    
    # Finds a path from the start to the end using backtracking.

    # Parameters:
    #  maze: The maze.
    #  cur_row: Current row.
    #  cur_col: Current column.
    #  size: Size of the maze.

    # Returns:
    # - True if a path is found, False otherwise.
    
    visited_cell = []
     # Those cell are already visited in previous function calls to find a path this visited_cell array store the values of their cur_row and cur_col. 

    def _find_path(cur_row, cur_col):
        nonlocal visited_cell

        if cur_row < 0 or cur_row >= size or cur_col < 0 or cur_col >= size or maze[cur_row][cur_col] == WALL or maze[cur_row][cur_col] == START or [cur_row, cur_col] in visited_cell:
            return False

        if maze[cur_row][cur_col] == END:
            return True

        # Explore in all directions
        maze[cur_row][cur_col] = PATH
        visited_cell.append([cur_row, cur_col])

        if _find_path(cur_row, cur_col + 1):
            return True

        if _find_path(cur_row + 1, cur_col):
            return True

        if _find_path(cur_row, cur_col - 1):
            return True

        if _find_path(cur_row - 1, cur_col):
            return True

        maze[cur_row][cur_col] = OPEN_SPACE  # Backtrack
        visited_cell.pop()

        return False

    return _find_path(cur_row, cur_col)

def main():

    # while loop will run till the user doesn't want to exit the game.
    while True:
        n = int(input("Enter the size of the maze (n x n): "))

        # if value of "n" is Invalid.
        while n <= 1:
            print("\nInvalid input, Please enter the size of maze (n x n) > 1")
            n = int(input("\nEnter the size of the maze (n x n): "))

        maze = generate_maze(n)
        print("\nGenerated Maze:")
        print_maze(maze)

        user_choice = input("\n1. Print the path\n2. Generate another puzzle\n3. Exit the game\nEnter your choice (1/2/3): ")

        if user_choice == '1':
            # Find the path
            if maze[0][1] == OPEN_SPACE:
                if find_path(maze, 0, 1, n):
                    print("\nMaze with Path:")
                    print_maze(maze)
                else:
                    print("\nPath not found.")

            elif maze[1][0] == OPEN_SPACE:
                if find_path(maze, 1, 0, n):
                    print("\nMaze with Path:")
                    print_maze(maze)
                else:
                    print("\nPath not found.")

            else:
                print("\nPath not found.")

            user_choice = input("\n1. Generate another puzzle\n2. Exit the game\nEnter your choice (1/2): ")

            if user_choice == '1':
                continue
            elif user_choice == '2':
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        elif user_choice == '2':
            continue
        elif user_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()