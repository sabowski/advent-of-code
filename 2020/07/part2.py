import sys
import re

import pprint

luggage={}

#  found_bag=0
total_bags=0

def count_total_luggage(color, x):

    print(' <-- IN COUNT_TOTAL_LUGGAGE - {} {} bag(s)--> '.format(x, color))
    bag_count=0

    #  print(luggage[color].keys())
    pprint.pp(luggage[color])


    for bag, num in luggage[color].items():

        print('{} has {} {} bag(s)'.format(color, num, bag))

        #  print('  *** checking {} ***'.format(bag))
        if len(luggage[bag]) != 0:
            print('{} contains more bags'.format(bag))
            print('({}) adding {} to bag_count ({})'.format(color, x, bag_count))
            bag_count+=int(num)
            bag_count+=(count_total_luggage(bag,int(num))*int(num))
            #  print(' - {} {} bags'.format(luggage[color][bag], bag))
            #  return luggage[color][bag] + count_total_luggage(bag)
        else:
            print('{} contains no bags'.format(bag))
            #  print(luggage
            #  bag_color+=luggage[color][bag]
            #  print('returning {}*{}'.format(int(num),x))
            #  return int(luggage[color][bag])*int(num)
            print('adding {} to bag_count ({})'.format(int(num), color))
            bag_count+=int(num)

    print('returning {} for {}'.format(bag_count, color))
    return bag_count




for line in sys.stdin:
    x = line.strip().split(' contain ')
    bag_color = x[0][0:-5]
    luggage[bag_color] = {}

    for y in x[1].split(','):
        contains = y.lstrip() # .rstrip(' bags.')

        if contains[0].isdigit():
            thing = re.findall(r'^(\d+) (.*) bag.*$', contains)
            luggage[bag_color][thing[0][1]] = thing[0][0]

print(count_total_luggage('shiny gold',1))

exit()

for bag in luggage:
    found_bag=0
    for inner_bag in luggage[bag]:
        check_luggage('shiny gold', bag, luggage[bag])
    if found_bag==1:
        total_bags+=1

print(total_bags)
