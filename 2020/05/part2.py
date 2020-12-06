#  --- Day 5: Part Two ---

#  Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

#  It's a completely full flight, so your seat should be the only missing
#  boarding pass in your list. However, there's a catch: some of the seats at
#  the very front and back of the plane don't exist on this aircraft, so
#  they'll be missing from your list as well.

#  Your seat wasn't at the very front or back, though; the seats with IDs +1
#  and -1 from yours will be in your list.

#  What is the ID of your seat?

#  Your puzzle answer was 743.

import sys
import math

def split_range(r, y):

    if y in ['F', 'L']:
        return [r[0], r[0]+math.floor((r[1]-r[0])/2)]
    if y in ['B', 'R']:
        return [r[0]+math.ceil((r[1]-r[0])/2), r[1]]

seat_ids=[]

for line in sys.stdin:

    row_range=[0,127]
    col_range=[0,7]

    for x in line.strip():
        if x in [ 'F', 'B' ]:
            row_range = split_range(row_range, x)
        if x in [ 'L', 'R' ]:
            col_range = split_range(col_range, x)

    seat_id=(row_range[0]*8)+col_range[0]

    seat_ids.append(seat_id)

seat_ids.sort()

for x in range(len(seat_ids)):
    try:
        if seat_ids[x+1] - seat_ids[x] == 2:
            print('seat id: {}'.format(seat_ids[x]+1))
    except IndexError:
        next
