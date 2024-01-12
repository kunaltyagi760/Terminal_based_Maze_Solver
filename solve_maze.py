# Constants for maze characters
WALL = '\033[91m█\033[0m'  # Red color
OPEN_SPACE = '\033[94m◌\033[0m'  # Blue color
START = '\033[92mS\033[0m'  # Green color
END = '\033[92mE\033[0m'  # Green color
PATH = '\033[92m◍\033[0m'  # Green color

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