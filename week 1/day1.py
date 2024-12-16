left = []
right = []

with open('day1input.md', 'r') as file:
    for line in file:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))

l1 = sorted(left)
l2 = sorted(right)

diff = [abs(a - b) for a, b in zip(l1, l2)]

#sim_score = [n * sum(1 for m in l2 if n == m) for n in l1]
sim_score = []
for n in l1:
    times = 0
    for m in l2:
        if n == m:
            times += 1

    sim_score.append(n * times)

print(sum(diff), sum(sim_score))