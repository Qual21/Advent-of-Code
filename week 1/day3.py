import re

mul = r"mul\((\d+),(\d+)\)"
dont = r"don't\(\)"
do = r"do\(\)"

active = True
matches = []
with open("day3input.md", "r") as f:
    #matches = re.findall(r"mul\((\d+),(\d+)\)", f.read())
    content = f.read()
    expressions = re.findall(f"({mul}|{dont}|{do})", content)

    for expression in expressions:
        if re.match(dont, expression[0]):
            active = False
        elif re.match(do, expression[0]):
            active = True
        elif active and re.match(mul, expression[0]):
            match = re.match(mul, expression[0])
            if match:
                matches.append((match.group(1), match.group(2)))    


print(sum([int(match[0]) * int(match[1]) for match in matches]))