#fsearch xmas = 206, samx = 206
#rotatoed, 247, 244, counterclockwise 377, 427, clockwise 385, 453
matrix = []
rotated = []
for i in range(141):
    rotated.append([])

with open("day4input.md", "r") as f:
    for line in f:
        matrix.append(line.strip())
        for i in range(140):
            rotated[i].append(line[i])

for i in range(141):
    rotated[i] = "".join(rotated[i])
for r in rotated:
    print(r)

### Instead of doing this properly, I just did ctrl f xmas and samx
### rotated the matrix then ctrl f again and summed
### Next is rotating 45 and -45 degrees

def rotate_45(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated = [[] for _ in range(n + m - 1)]

    for i in range(n):
        for j in range(m):
            rotated[i + j].append(matrix[i][j])

    return rotated


#rotated_matrix = rotate_45(matrix)
#for row in rotated_matrix:
 #   print("".join(row))

def rotate_45_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated = [[] for _ in range(n + m - 1)]

    for i in range(n):
        for j in range(m):
            rotated[j - i + (n - 1)].append(matrix[i][j])

    return rotated


rotated_matrix = rotate_45_clockwise(matrix)
for row in rotated_matrix:
    print("".join(row))
