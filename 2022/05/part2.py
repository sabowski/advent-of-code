# --- Part Two ---
#
# As you watch the crane operator expertly rearrange the crates, you notice the
# process isn't following your prediction.
#
# Some mud was covering the writing on the side of the crane, and you quickly
# wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
#
# The CrateMover 9001 is notable for many new and exciting features: air
# conditioning, leather seats, an extra cup holder, and the ability to pick up
# and move multiple crates at once.
#
# Again considering the example above, the crates begin in the same
# configuration:
#
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# Moving a single crate from stack 2 to stack 1 behaves the same as before:
#
# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# However, the action of moving three crates from stack 1 to stack 3 means that
# those three moved crates stay in the same order, resulting in this new
# configuration:
#
#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
#
# Next, as both crates are moved from stack 2 to stack 1, they retain their
# order as well:
#
#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
#
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's
# crate C that gets moved:
#
#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
#
# In this example, the CrateMover 9001 has put the crates in a totally
# different order: MCD.
#
# Before the rearrangement process finishes, update your simulation so that the
# Elves know where they should stand to be ready to unload the final supplies.
# After the rearrangement procedure completes, what crate ends up on top of
# each stack?

# crates = {
#     1: [ 'Z', 'N' ],
#     2: [ 'M', 'C', 'D' ],
#     3: [ 'P' ]
# }

crates = {
    1: [ 'P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T' ],
    2: [ 'H', 'F', 'R' ],
    3: [ 'P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D' ],
    4: [ 'Q', 'H', 'P', 'B', 'F', 'W', 'G' ],
    5: [ 'P', 'S', 'M', 'J', 'H' ],
    6: [ 'M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L' ],
    7: [ 'P', 'T', 'H', 'N', 'M', 'L' ],
    8: [ 'F', 'D', 'Q', 'R' ],
    9: [ 'D', 'S', 'C', 'N', 'L', 'P', 'H' ]
}

with open('input.txt') as fd:
    for line in fd:
        if line.startswith("move"):
            x = line.strip().split()
            qty = int(x[1])
            source = int(x[3])
            target = int(x[5])
            temp = []
            for i in range(0, qty):
                temp.append(crates[source].pop())
            for i in range(0, qty):
                crates[target].append(temp.pop())
final = ""
for crate in crates:
    final += crates[crate][-1]
print(f"{final}")
