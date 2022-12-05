# --- Part Two ---
#
# It seems like there is still quite a bit of duplicate work planned. Instead,
# the Elves would like to know the number of pairs that overlap at all.
#
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't
# overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and
# 2-6,4-8) do overlap:
#
#     - 5-7,7-9 overlaps in a single section, 7.
#     - 2-8,3-7 overlaps all of the sections 3 through 7.
#     - 6-6,4-6 overlaps in a single section, 6.
#     - 2-6,4-8 overlaps in sections 4, 5, and 6.
#
# So, in this example, the number of overlapping assignment pairs is 4.
#
# In how many assignment pairs do the ranges overlap?

running_total = 0
with open('input.txt') as fd:
    for line in fd:
        a, b = line.strip().split(',')
        x = range(int(a.split("-")[0]), int(a.split("-")[1])+1)
        y = range(int(b.split("-")[0]), int(b.split("-")[1])+1)
        z = set(x).intersection(set(y))
        if z:
            running_total += 1
print(f"{running_total}")
