import sys
import re

import pprint

luggage={}

found_bag=0
total_bags=0

def check_luggage(color, outer_bag, inner_bags):

    global found_bag

    if color in inner_bags.keys():
        found_bag=1
        return True
    else:
        for bag in inner_bags:
            check_luggage(color, bag, luggage[bag])

for line in sys.stdin:
    x = line.strip().split(' contain ')
    bag_color = x[0][0:-5]
    luggage[bag_color] = {}

    for y in x[1].split(','):
        contains = y.lstrip() # .rstrip(' bags.')

        if contains[0].isdigit():
            thing = re.findall(r'^(\d+) (.*) bag.*$', contains)
            luggage[bag_color][thing[0][1]] = thing[0][0]

for bag in luggage:
    found_bag=0
    for inner_bag in luggage[bag]:
        check_luggage('shiny gold', bag, luggage[bag])
    if found_bag==1:
        total_bags+=1

print(total_bags)
