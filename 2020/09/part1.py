import sys

xmas=[]
preamble = 25

for line in sys.stdin:
    curr = int(line.strip())

    if len(xmas) < preamble:
        xmas.append(int(curr))
        continue

    match = False

    for x in xmas:
        if curr - x == x:
            continue

        if curr - x in xmas:
            match = True
            break

    if match:
        xmas.pop(0)
        xmas.append(curr)
    else:
        print(curr)
        exit()
