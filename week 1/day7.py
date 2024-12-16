result = []

with open('day7input.md', 'r') as file:
    for line in file:
        line = line.strip()
        first_num, rest_of_nums = line.split(':')
        first_num = int(first_num)
        rest_of_nums = list(map(int, rest_of_nums.split()))
        result.append((first_num, rest_of_nums))

correct = []
correct_result = []

for r in result:
    goal = r[0]
    numbers = r[1]

    total = [numbers[0]]

    for n in numbers[1:]:
        next_total = []
        
        for t in total:
            next_total.append(t * n)
            next_total.append(t + n)
            next_total.append(t * (10 ** len(str(n))) + n)

        total = next_total

    if goal in total:
        correct.append(r)
        correct_result.append(goal)

print(sum(correct_result))

