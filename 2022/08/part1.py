# --- Day 8: Treetop Tree House ---
#
# The expedition comes across a peculiar patch of tall trees all planted
# carefully in a grid. The Elves explain that a previous expedition planted
# these trees as a reforestation effort. Now, they're curious if this would be
# a good location for a tree house.
#
# First, determine whether there is enough tree cover here to keep a tree house
# hidden. To do this, you need to count the number of trees that are visible
# from outside the grid when looking directly along a row or column.
#
# The Elves have already launched a quadcopter to generate a map with the
# height of each tree (your puzzle input). For example:
#
# 30373
# 25512
# 65332
# 33549
# 35390
#
# Each tree is represented as a single digit whose value is its height, where 0
# is the shortest and 9 is the tallest.
#
# A tree is visible if all of the other trees between it and an edge of the
# grid are shorter than it. Only consider trees in the same row or column; that
# is, only look up, down, left, or right from any given tree.
#
# All of the trees around the edge of the grid are visible - since they are
# already on the edge, there are no trees to block the view. In this example,
# that only leaves the interior nine trees to consider:
#
#     - The top-left 5 is visible from the left and top. (It isn't visible from
#       the right or bottom since other trees of height 5 are in the way.)
#     - The top-middle 5 is visible from the top and right.
#     - The top-right 1 is not visible from any direction; for it to be
#       visible, there would need to only be trees of height 0 between it and an
#       edge.
#     - The left-middle 5 is visible, but only from the right.
#     - The center 3 is not visible from any direction; for it to be visible,
#       there would need to be only trees of at most height 2 between it and an
#       edge.
#     - The right-middle 3 is visible from the right.
#     - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
#
# With 16 trees visible on the edge and another 5 visible in the interior, a
# total of 21 trees are visible in this arrangement.
#
# Consider your map; how many trees are visible from outside the grid?

trees = []
with open('input.txt') as fd:
    for line in fd:
        trees.append(line.strip())

num_rows = len(trees)
num_cols = len(trees[0])
curr_row = 0
running_count = 0

for row in trees:
    curr_row += 1
    if curr_row == 1 or curr_row == num_rows:
        running_count += len(row)
    else:
        curr_col = 0
        for col in row:
            curr_col += 1
            if curr_col == 1 or curr_col == num_cols:
                running_count += 1
            else:
                results = []
                curr_tree = trees[curr_row - 1][curr_col -1]
                row_s = trees[curr_row - 1]
                col_s = ""
                for x in range(0,num_rows):
                    col_s += trees[x][curr_col - 1]

                # row
                row_west = row_s[0:curr_col-1]
                row_east = row_s[curr_col:num_cols]
                results.append(all(i < curr_tree for i in row_west))
                results.append(all(i < curr_tree for i in row_east))

                # col
                col_north = col_s[0:curr_row-1]
                col_south = col_s[curr_row:num_rows]
                results.append(all(i < curr_tree for i in col_north))
                results.append(all(i < curr_tree for i in col_south))

                if True in results:
                    running_count += 1

print(f"{running_count}")
