#  --- Day 3: Part Two ---

#  Time to check the rest of the slopes - you need to minimize the probability
#  of a sudden arboreal stop, after all.

#  Determine the number of trees you would encounter if, for each of the
#  following slopes, you start at the top-left corner and traverse the map all
#  the way to the bottom:

    #  Right 1, down 1.
    #  Right 3, down 1. (This is the slope you already checked.)
    #  Right 5, down 1.
    #  Right 7, down 1.
    #  Right 1, down 2.

#  In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
#  respectively; multiplied together, these produce the answer 336.

#  What do you get if you multiply together the number of trees encountered on
#  each of the listed slopes?

# answer: 4355551200

map = []

with open('input.txt') as fd:
    for row in fd:
        map.append(row.rstrip('\n'))

slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]
answer = 1

for slope in slopes:

    x_pos = 0
    trees = 0

    for line in map[slope[1]::slope[1]]:

        try:
            line[x_pos+slope[0]]
            x_pos+=slope[0]
        except IndexError:
            x_pos=x_pos+slope[0]-len(line)

        if line[x_pos] == '#':
            trees+=1

    print('slope {} trees: {}'.format(slope,trees))
    answer*=trees

print(answer)
