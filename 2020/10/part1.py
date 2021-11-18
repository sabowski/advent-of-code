import sys

adapters=[]
joltage=0
diffs=[0,0,1]

for line in sys.stdin:
    adapters.append(int(line.strip()))


while len(adapters) > 0:

    #  print(len(adapters))
    #  print(diffs)

    for x in [ 1, 2, 3 ]:
        #  print('{} + {}'.format(joltage,x))
        if joltage + x in adapters:
            diffs[x-1]+=1
            adapters.pop(adapters.index(joltage+x))
            joltage+=x
            break

print(diffs[0]*diffs[2])



