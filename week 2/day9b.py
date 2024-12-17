import time

dense = ""
with open('day9input.md', 'r') as file:
    dense = file.read()

clever = []
for i, n in enumerate(dense):
    if i & 1 == 0:
        for j in range(int(n)):
            clever.append(i//2)
    else:
        for j in range(int(n)):
            clever.append('.')


#print(clever)
def swap_files(clever):
    i = len(clever) - 1
    j = 0
    while i >= j:
        if clever[i] != '.':
            while j < i and clever[j] != '.':
                j += 1
            if j > i:
                break
            clever[i], clever[j] = clever[j], clever[i]
        i -= 1

    return clever

start_time = time.time()
clever = swap_files(clever)


total = 0
for i, n in enumerate(clever):
    if n == '.':
        break
    total += int(n) * i

end_time = time.time()
print (total, end_time - start_time)