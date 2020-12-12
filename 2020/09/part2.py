import sys

xmas=[]
xmas_all=[]
preamble = 25
bad_num = None

for line in sys.stdin:
    curr = int(line.strip())

    xmas_all.append(curr)

    if bad_num == None:

        if len(xmas) < preamble:
            xmas.append(int(curr))
            continue

        match = False

        for x in xmas:
            if curr - x == x:
                continue

            if curr - x in xmas:
                match = True
                break

        if match:
            xmas.pop(0)
            xmas.append(curr)
        else:
            bad_num = curr

print(xmas_all)
print(bad_num)

for x in range(len(xmas_all)):

    print('<><> INDEX: {} <><>'.format(x))

    #  correct_sum = None
    running_sum = xmas_all[x]
    #  smallest = xmas_all[x]
    y = 1

    print('starting running sum {}'.format(running_sum))

    while running_sum < bad_num:
        print('running sum ({}) less than bad_num ({})'.format(running_sum,bad_num))
        print('next number is {}'.format(xmas_all[x+y]))
        running_sum+=xmas_all[x+y]
        print('new running sum {}'.format(running_sum))
        y+=1
        continue

    if running_sum > bad_num:
        continue

    if running_sum == bad_num:
        # we got it
        #  nums = xmas_all[x:x+y]
        print(min(xmas_all[x:x+y])+max(xmas_all[x:x+y]))
        #  print(nums)
        break

    #  if running_sum < bad_num:


    print(xmas_all[x])
