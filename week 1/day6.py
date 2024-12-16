### I chose to rotate the matrix rather than turning right just for fun
### This requires massively more computation, so is not recommended
### I did the second part on a different machine without rotation
### If I remember where, I'll add it. Potentially redo it.

maze = []

with open("day6input.md", "r") as f:
    for line in f:
        maze.append(list(line.strip()))

line = 0
start = 0

for m in maze:
    line += 1
    for n in m:
        if n == "^":
            start = (line-1, m.index(n))
            break



def rotate_matrix_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_matrix_counterclockwise(matrix):
    n = len(matrix)
    return [[matrix[j][n - 1 - i] for j in range(n)] for i in range(n)]

rotated = 0
while rotated < 200:
    if start[0] - 1 < 0:
        print("Escaped")
        break
    if maze[start[0]-1][start[1]] != "#":
        maze[start[0]-1][start[1]] = "X"
        start = (start[0] - 1, start[1])
        
    else:
        maze = rotate_matrix_counterclockwise(maze)
        start = (len(maze) - 1 - start[1], start[0])
        rotated += 1
    

for m in maze:
    print(''.join(m))

tally = 0
for m in maze:
    for n in m:
        if n == "X":
            tally += 1

print(tally, rotated)
            