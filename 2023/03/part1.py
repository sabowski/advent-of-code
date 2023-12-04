# --- Day 3: Gear Ratios ---
#
# You and the Elf eventually reach a gondola lift station; he says the gondola
# lift will take you up to the water source, but this is as far as he can bring
# you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be a problem:
# they're not moving.
#
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of
# surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
# right now; it'll still be a while before I can fix it." You offer to help.
#
# The engineer explains that an engine part seems to be missing from the
# engine, but nobody can figure out which one. If you can add up all the part
# numbers in the engine schematic, it should be easy to work out which part is
# missing.
#
# The engine schematic (your puzzle input) consists of a visual representation
# of the engine. There are lots of numbers and symbols you don't really
# understand, but apparently any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included in your sum. (Periods (.) do not
# count as a symbol.)
#
# Here is an example engine schematic:
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
# In this schematic, two numbers are not part numbers because they are not
# adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
# number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all
# of the part numbers in the engine schematic?

import sys

schematic = []
x = -1
total = 0

for line in sys.stdin:
    schematic.append(line.rstrip())

for line in schematic:
    x += 1
    part_no = ''
    is_part_no = False
    for y in range(len(line)):

        if schematic[x][y].isdigit():
            part_no += schematic[x][y]
            if not is_part_no:
                if x > 0 and y > 0:
                    if not schematic[x-1][y-1].isalnum() and schematic[x-1][y-1] != '.':
                        is_part_no = True

                if y > 0:
                    if not schematic[x][y-1].isalnum() and schematic[x][y-1] != '.':
                        is_part_no = True
                    try:
                        if not schematic[x+1][y-1].isalnum() and schematic[x+1][y-1] != '.':
                            is_part_no = True
                    except IndexError:
                        pass

                if x > 0:
                    if not schematic[x-1][y].isalnum() and schematic[x-1][y] != '.':
                        is_part_no = True
                    try:
                        if not schematic[x-1][y+1].isalnum() and schematic[x-1][y+1] != '.':
                            is_part_no = True
                    except IndexError:
                        pass

                try:
                    if not schematic[x+1][y].isalnum() and schematic[x+1][y] != '.':
                        is_part_no = True
                except IndexError:
                    pass

                try:
                    if not schematic[x][y+1].isalnum() and schematic[x][y+1] != '.':
                        is_part_no = True
                except IndexError:
                    pass

                try:
                    if not schematic[x+1][y+1].isalnum() and schematic[x+1][y+1] != '.':
                        is_part_no = True
                except IndexError:
                    pass

            if y+1 == len(line) and is_part_no:
                total += int(part_no)

        elif not schematic[x][y].isdigit() and not is_part_no:
            part_no = ''
            continue

        else:
            total += int(part_no)
            part_no = ''
            is_part_no = False
        
print(total)
