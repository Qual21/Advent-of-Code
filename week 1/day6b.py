# Load the maze from file
maze = []

with open("day6input.md", "r") as f:
    for line in f:
        maze.append(list(line.strip()))

line = 0
start = 0
clean_maze = [row.copy() for row in maze]

# Find the starting position of the robot
for m in maze:
    line += 1
    for n in m:
        if n == "^":
            start = (line-1, m.index(n))
            break

fresh_start = start

# Set up tracking for visited positions
visited = set()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
direction_index = 0  # Initial direction is up (index 0)

rotated = 0  # Keep track of the number of rotations
while rotated < 2000:
    if (start, direction_index) in visited:
        print("Robot is stuck in an infinite loop!")
        break
    visited.add((start, direction_index))
    
    # Calculate the next cell based on the current direction
    next_row = start[0] + directions[direction_index][0]
    next_col = start[1] + directions[direction_index][1]
    
    # Check if the next cell is outside the maze (escape condition)
    if next_row < 0 or next_row >= len(maze) or next_col < 0 or next_col >= len(maze[0]):
        print("Escaped")
        break

    # Check if the next cell is not an obstacle
    if maze[next_row][next_col] != "#":
        # Move to the next cell
        start = (next_row, next_col)
        maze[start[0]][start[1]] = "X"  # Mark the new position as visited
    else:
        # Turn right: update the direction index
        direction_index = (direction_index + 1) % 4
        rotated += 1

# Identify visited squares
squares = []
for m_idx, m in enumerate(maze):
    for n_idx, n in enumerate(m):
        if n == "X":
            squares.append((m_idx, n_idx))

# Test each visited square by adding a single obstacle and checking for loops
loops = []
for square in squares:
    # Create a fresh copy of the clean maze
    cleaner_maze = [row.copy() for row in clean_maze]
    
    # Add an obstacle at the current square
    cleaner_maze[square[0]][square[1]] = "#"

    # Reset the start position for the test
    start = fresh_start  # Reset the starting point
    
    # Initialize tracking for this test
    visited2 = set()
    direction_index = 0  # Initial direction is up
    rotated2 = 0  # Rotation counter

    while rotated2 < 2000:
        if (start, direction_index) in visited2:
            print(f"Robot is stuck in an infinite loop when obstacle is at {square}!")
            loops.append(square)
            break
        visited2.add((start, direction_index))
    
        # Calculate the next cell based on the current direction
        next_row = start[0] + directions[direction_index][0]
        next_col = start[1] + directions[direction_index][1]
    
        # Check if the next cell is outside the maze (escape condition)
        if next_row < 0 or next_row >= len(cleaner_maze) or next_col < 0 or next_col >= len(cleaner_maze[0]):
            print("Escaped")
            break

        # Check if the next cell is not an obstacle
        if cleaner_maze[next_row][next_col] != "#":
            start = (next_row, next_col)
            cleaner_maze[start[0]][start[1]] = "X"
        else:
            # Turn right: update the direction index
            direction_index = (direction_index + 1) % 4
            rotated2 += 1

print(len(loops))
