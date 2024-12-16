matrix = []

with open('day8input.md', 'r') as file:
    for line in file:
        matrix.append(line.strip())


length = len(matrix)
antenna = []

for i, line in enumerate(matrix):
    for j, e in enumerate(line):
        if e != '.':
            antenna.append((matrix[i][j], i, j))

def is_within_bounds(x, y, length):
    return 0 <= x < length and 0 <= y < length

antinodes = set()

for i, a in enumerate(antenna):
    symbol_a, y1, x1 = a
    antinodes.add((x1, y1))
    for j, b in enumerate(antenna):
        if i >= j:  # Avoid duplicate pairings and self-pairing
            continue
        
        symbol_b, y2, x2 = b
        
        if symbol_a == symbol_b:

            distance_x = abs(x1 - x2)
            distance_y = abs(y1 - y2)
            
            if x1 < x2:
                antinode1_x = x1 - distance_x
                antinode1_y = y1 - distance_y
                antinode2_x = x2 + distance_x
                antinode2_y = y2 + distance_y
            else:
                antinode1_x = x1 + distance_x
                antinode1_y = y1 - distance_y
                antinode2_x = x2 - distance_x
                antinode2_y = y2 + distance_y
            
            antinode1 = (antinode1_x, antinode1_y)
            antinode2 = (antinode2_x, antinode2_y)
            
            if is_within_bounds(antinode1[0], antinode1[1], length):
                antinodes.add(antinode1)
            if is_within_bounds(antinode2[0], antinode2[1], length):
                antinodes.add(antinode2)

            multiplier = 1
            while 1:
                if x1 < x2:
                    harmonic1_x = x1 - (multiplier * distance_x)
                    harmonic1_y = y1 - (multiplier * distance_y)
                    harmonic2_x = x2 + (multiplier * distance_x)
                    harmonic2_y = y2 + (multiplier * distance_y)
                else:
                    harmonic1_x = x1 + (multiplier * distance_x)
                    harmonic1_y = y1 - (multiplier * distance_y)
                    harmonic2_x = x2 - (multiplier * distance_x)
                    harmonic2_y = y2 + (multiplier * distance_y)
                
                if is_within_bounds(harmonic1_x, harmonic1_y, length):
                    antinodes.add((harmonic1_x, harmonic1_y))
                if is_within_bounds(harmonic2_x, harmonic2_y, length):
                    antinodes.add((harmonic2_x, harmonic2_y))

                if not is_within_bounds(harmonic1_x, harmonic1_y, length) and not is_within_bounds(harmonic2_x, harmonic2_y, length):
                    break
                multiplier += 1

print(len(antinodes))