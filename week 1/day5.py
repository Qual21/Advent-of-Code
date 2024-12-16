pages = []
updates = []

with open("day5input.md", "r") as f:
    for line in f:
        pages.append((int(line[0:2]), int(line[3:5])))
        pass

with open("day5input2.md", "r") as f:
    lines = f.readlines()

updates = [list(map(int, line.strip().split(','))) for line in lines]

def sort(update):
    if not update:
        return []
    left = []
    right = []

    for a, b in pages:
        if a == update[0]:
            if b in update:
                right.append(b)
    for u in update:
        if u not in right and u != update[0]:
            left.append(u)

    
    return sort(left) + [update[0]] + sort(right)

total = 0
wrong_total = 0
for update in updates:
    if update == sort(update):
        total += sort(update)[len(sort(update))//2]
    else:
        wrong_total += sort(update)[len(sort(update))//2]
print(total, wrong_total)