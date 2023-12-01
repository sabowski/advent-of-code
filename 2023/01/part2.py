# --- Part Two ---
#
# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first and
# last digit on each line. For example:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
#
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.
#
# What is the sum of all of the calibration values?

import sys

total = 0

lines_processed = 0

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in sys.stdin:
    c = line.rstrip()

    i = 0
    z = ''
    while True:
        if i > len(c)-1:
            break

        if c[i].isdigit():
            z += c[i]
            i += 1
            continue

        for num in num_dict:
            if c[i:].startswith(num):
                z += num_dict[num]
        i += 1

    calib = int(f"{z[0]}{z[-1]}")
    total += calib
    lines_processed += 1

print(total)
