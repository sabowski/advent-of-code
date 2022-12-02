# --- Part Two ---
#
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
# the second column says how the round needs to end: X means you need to lose,
# Y means you need to end the round in a draw, and Z means you need to win.
# Good luck!"
#
# The total score is still calculated in the same way, but now you need to
# figure out what shape to choose so the round ends as indicated. The example
# above now goes like this:
#
#     - In the first round, your opponent will choose Rock (A), and you need
#       the round to end in a draw (Y), so you also choose Rock. This gives you
#       a score of 1 + 3 = 4.
#     - In the second round, your opponent will choose Paper (B), and you
#       choose Rock so you lose (X) with a score of 1 + 0 = 1.
#     - In the third round, you will defeat your opponent's Scissors with Rock
#       for a score of 1 + 6 = 7.
#
# Now that you're correctly decrypting the ultra top secret strategy guide, you
# would get a total score of 12.
#
# Following the Elf's instructions for the second column, what would your total
# score be if everything goes exactly according to your strategy guide?


key = [
    [ 2, 1, 0 ],
    [ 0, 2, 1 ],
    [ 1, 0, 2 ]
]

player1 = {
    "A": 0,
    "B": 1,
    "C": 2
}

expected_result = {
    "X": 0,
    "Y": 2,
    "Z": 1
}

shape_point = [ 1, 2, 3 ]

result_point = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

running_total = 0

with open('input.txt') as fd:
    for line in fd:
        plays = line.split()
        running_total += shape_point[key[player1[plays[0]]].index(expected_result[plays[1]])]
        running_total += result_point[plays[1]]
print(f"{running_total}")

