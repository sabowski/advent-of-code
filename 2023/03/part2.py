# --- Part Two ---
#
# The engineer finds the missing part and installs it in the engine! As the
# engine springs to life, you jump in the closest gondola, finally ready to
# ascend to the water source.
#
# You don't seem to be going very fast, though. Maybe something is still wrong?
# Fortunately, the gondola has a phone labeled "help", so you pick it up and
# the engineer answers.
#
# Before you can explain the situation, she suggests that you look out the
# window. There stands the engineer, holding a phone in one hand and waving
# with the other. You're going so slowly that you haven't even left the
# station. You exit the gondola.
#
# The missing part wasn't the only issue - one of the gears in the engine is
# wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
#
# This time, you need to find the gear ratio of every gear and add them all up
# so that the engineer can figure out which gear needs to be replaced.
#
# Consider the same engine schematic again:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# In this schematic, there are two gears. The first is in the top left; it has
# part numbers 467 and 35, so its gear ratio is 16345. The second gear is in
# the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a
# gear because it is only adjacent to one part number.) Adding up all of the
# gear ratios produces 467835.
#
# What is the sum of all of the gear ratios in your engine schematic?
#

import sys
import math

schematic = []
x = -1
total = 0

def get_surrounding_digits(x,y):
    num = schematic[x][y]
    offset = 1
    while True:
        if y - offset >= 0 and schematic[x][y-offset].isdigit():
            num = schematic[x][y-offset] + num
        else:
            break
        offset += 1
        
    offset = 1
    while True:
        try:
            if schematic[x][y+offset].isdigit():
                num = num + schematic[x][y+offset]
            else:
                break
        except IndexError:
            break

        offset += 1

    return num


for line in sys.stdin:
    schematic.append(line.rstrip())

for line in schematic:
    x += 1
    for y in range(len(line)):
        part_nos = []

        if schematic[x][y] == '*':

            # check above
            if x > 0:
                if schematic[x-1][y].isdigit():
                    part_nos.append(int(get_surrounding_digits(x-1,y)))
                else:
                    if schematic[x-1][y-1].isdigit():
                        part_nos.append(int(get_surrounding_digits(x-1,y-1)))
                    try:
                        if schematic[x-1][y+1].isdigit():
                            part_nos.append(int(get_surrounding_digits(x-1,y+1)))
                    except IndexError:
                        pass

            # check to left
            if y > 0:
                if schematic[x][y-1].isdigit():
                    part_nos.append(int(get_surrounding_digits(x,y-1)))

            # check to right
            try:
                if schematic[x][y+1].isdigit():
                    part_nos.append(int(get_surrounding_digits(x,y+1)))
            except IndexError:
                pass

            # check below
            try:
                if schematic[x+1][y].isdigit():
                    part_nos.append(int(get_surrounding_digits(x+1,y)))
                else:
                    if y>0 and schematic[x+1][y-1].isdigit():
                        part_nos.append(int(get_surrounding_digits(x+1,y-1)))
                    if schematic[x+1][y+1].isdigit():
                        part_nos.append(int(get_surrounding_digits(x+1,y+1)))
            except IndexError:
                pass

        if len(part_nos) == 2:
            total += math.prod(part_nos)
            part_nos = []
        
print(total)
