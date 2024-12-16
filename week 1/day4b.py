matrix = []

with open('day4input.md', 'r') as file:
    for line in file:
        matrix.append(line.strip())

counr = 0
for i in range(len(matrix) -2):
    for j in range(len(matrix[i]) - 2):
        if (matrix[i][j] == 'M' and matrix[i][j+2] == 'M' and matrix[i+1][j+1] == 'A'
        and matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'S'):
            counr += 1
        if (matrix[i][j] == 'S' and matrix[i][j+2] == 'S' and matrix[i+1][j+1] == 'A'
        and matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'M'):
            counr += 1
        if (matrix[i][j] == 'M' and matrix[i][j+2] == 'S' and matrix[i+1][j+1] == 'A'
        and matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'S'):
            counr += 1
        if (matrix[i][j] == 'S' and matrix[i][j+2] == 'M' and matrix[i+1][j+1] == 'A'
        and matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'M'):
            counr += 1

print(counr)