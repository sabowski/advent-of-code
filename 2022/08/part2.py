# --- Part Two ---
#
# Content with the amount of tree cover available, the Elves just need to know
# the best spot to build their tree house: they would like to be able to see a
# lot of trees.
#
# To measure the viewing distance from a given tree, look up, down, left, and
# right from that tree; stop if you reach an edge or at the first tree that is
# the same height or taller than the tree under consideration. (If a tree is
# right on the edge, at least one of its viewing distances will be zero.)
#
# The Elves don't care about distant trees taller than those found by the rules
# above; the proposed tree house has large eaves to keep it dry, so they
# wouldn't be able to see higher than the tree house anyway.
#
# In the example above, consider the middle 5 in the second row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
#
#     - Looking up, its view is not blocked; it can see 1 tree (of height 3).
#     - Looking left, its view is blocked immediately; it can see only 1 tree
#       (of height 5, right next to it).
#     - Looking right, its view is not blocked; it can see 2 trees.
#     - Looking down, its view is blocked eventually; it can see 2 trees (one
#       of height 3, then the tree of height 5 that blocks its view).
#
# A tree's scenic score is found by multiplying together its viewing distance
# in each of the four directions. For this tree, this is 4 (found by
# multiplying 1 * 1 * 2 * 2).
#
# However, you can do even better: consider the tree of height 5 in the middle
# of the fourth row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
#
#     - Looking up, its view is blocked at 2 trees (by another tree with a
#       height of 5).
#     - Looking left, its view is not blocked; it can see 2 trees.
#     - Looking down, its view is also not blocked; it can see 1 tree.
#     - Looking right, its view is blocked at 2 trees (by a massive tree of
#       height 9).
#
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the
# tree house.
#
# Consider each tree on your map. What is the highest scenic score possible for
# any tree?

import math
trees = []
with open('input.txt') as fd:
    for line in fd:
        trees.append(line.strip())

num_rows = len(trees)
num_cols = len(trees[0])
curr_row = 0
running_score = 0

for row in trees:
    curr_row += 1
    if curr_row != 1 or curr_row != num_rows:
        curr_col = 0
        for col in row:
            curr_col += 1
            if curr_col != 1 or curr_col != num_cols:
                results = []
                curr_tree = trees[curr_row - 1][curr_col -1]
                row_s = trees[curr_row - 1]
                col_s = ""
                for x in range(0,num_rows):
                    col_s += trees[x][curr_col - 1]

                # row
                row_west = row_s[0:curr_col-1]
                count = 0
                for x in reversed(row_west):
                    count += 1
                    if x >= curr_tree:
                        break
                results.append(count)
                    
                row_east = row_s[curr_col:num_cols]
                count = 0
                for x in row_east:
                    count += 1
                    if x >= curr_tree:
                        break
                results.append(count)

                # col
                col_north = col_s[0:curr_row-1]
                count = 0
                for x in reversed(col_north):
                    count += 1
                    if x >= curr_tree:
                        break
                results.append(count)

                col_south = col_s[curr_row:num_rows]
                count = 0
                for x in col_south:
                    count += 1
                    if x >= curr_tree:
                        break
                results.append(count)

                score = math.prod(results)
                if score > running_score:
                    running_score = score

print(f"{running_score}")
