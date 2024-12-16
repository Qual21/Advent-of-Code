safe = 0
safe_list = []
safe1 = 0

with open("day2input.md", "r") as f:
    for line in f:
        numbers = list(map(int, line.split()))

        def check_safety(numbers):
            if all(1 <= (numbers[i+1] - numbers[i]) <= 3 for i in range(len(numbers) - 1)):
                return True
            if all(1 <= (numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1)):
                return True
            return False

        def is_safe_with_one_skip(numbers):
            for i in range(len(numbers)):
                if check_safety(numbers[:i] + numbers[i+1:]):
                    return True
            return False

        if check_safety(numbers):
            safe += 1
            safe_list.append(numbers)
        if is_safe_with_one_skip(numbers):
            safe1 += 1

print(f"Number of safe lines: {safe}")
print(f"Number of safe lines with one skip: {safe1}")
