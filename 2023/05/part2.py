# --- Part Two ---
#
# Everyone will starve if you only plant such a small number of seeds.
# Re-reading the almanac, it looks like the seeds: line actually describes
# ranges of seed numbers.
#
# The values on the initial seeds: line come in pairs. Within each pair, the
# first value is the start of the range and the second value is the length of
# the range. So, in the first line of the example above:
#
# seeds: 79 14 55 13
#
# This line describes two ranges of seed numbers to be planted in the garden.
# The first range starts with seed number 79 and contains 14 values: 79, 80,
# ..., 91, 92. The second range starts with seed number 55 and contains 13
# values: 55, 56, ..., 66, 67.
#
# Now, rather than considering four seed numbers, you need to consider a total
# of 27 seed numbers.
#
# In the above example, the lowest location number can be obtained from seed
# number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77,
# temperature 45, humidity 46, and location 46. So, the lowest location number
# is 46.
#
# Consider all of the initial seed numbers listed in the ranges on the first
# line of the almanac. What is the lowest location number that corresponds to
# any of the initial seed numbers?

import sys
import threading
from datetime import datetime

srcs = []
dests = []
maps = {}
map_no = 0
lowest_locations = []
first_start = datetime.now()

def do_range(start, length):

    print(f'{threading.current_thread().name} started\tstart: {start}\tlength: {length}')

    location_no = -1
    time_start = datetime.now()

    for seed in range(start, start+length):
        found_dest = False

        src = seed
        for map in list(maps.keys()):
            found_dest = False

            for map_line in maps[map]:
                src_range = range(map_line[1], map_line[1]+map_line[2])

                if src in src_range:
                    destx = map_line[0] + (src - map_line[1])
                    # print(f'    source is covered in this map: {src} -> {destx}')
                    found_dest = True
                    src = destx
                    break

            if found_dest:
                continue

        if location_no == -1:
            location_no = src
        else:
            if location_no > src:
                location_no = src

        if (datetime.now() - time_start).seconds == 5:
            completed = round((seed - start)/length*100,2)
            print(f'thread {threading.current_thread().name} \ttime since start: {round((datetime.now() - first_start).seconds/3600,2)}h\t{completed}% complete')
            time_start = datetime.now()

    with threading.Lock():
        lowest_locations.append(location_no)
    print(f'{threading.current_thread().name} out!')

# get seed ranges
seed_ranges = [int(i) for i in sys.stdin.readline().split(':')[1].split()]
sys.stdin.readline()

# get maps
for line in sys.stdin:
    if line[0].isalpha():
        # only the first line starts with 'seeds'
        map_no += 1
        maps[map_no] = []

    if line[0].isnumeric():
        maps[map_no].append([int(i) for i in line.split()])

threads = list()
thread_index = 0
for seed_range in range(0, len(seed_ranges), 2):
    thread_index += 1
    thread = threading.Thread(target=do_range, name=f'thread {thread_index}', args=[seed_ranges[seed_range],seed_ranges[seed_range+1]])
    threads.append(thread)
    thread.start()

for index, thread in enumerate(threads):
    thread.join()

print(lowest_locations)
print(min(lowest_locations))
