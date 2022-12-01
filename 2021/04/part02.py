# On the other hand, it might be wise to try a different strategy: let the
# giant squid win.
# 
# You aren't sure how many bingo boards a giant squid could play at once, so
# rather than waste time counting its arms, the safe thing to do is to figure
# out which board will win last and choose that one. That way, no matter which
# boards it picks, it will win for sure.
# 
# In the above example, the second board is the last to win, which happens
# after 13 is eventually called and its middle column is completely marked. If
# you were to keep playing until this point, the second board would have a sum
# of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
# 
# Figure out which board will win last. Once it wins, what would its final
# score be?

from pprint import pprint

cards = []
tmp_card = []

def check_for_bingo(numbers, card):

    for line in card:
        #  print('new line in card (row)')
        common = set(line).intersection(numbers[:num])
        if len(common) == 5:
            #  curr_card = card.copy()
            #  found = True
            print("ROW MATCH!")
            return True
    #  if found:
        #  print('found a row so breaking')
        #  break
    #  print('rotated')
    for line in list(zip(*card[::-1])):
        print('new line in card (col)')
        #  print(type(line))
        common = set(line).intersection(numbers[:num])
        if len(common) == 5:
            #  curr_card = card.copy()
            #  found = True
            print("COLUMN MATCH")
            return True

    return False


#  with open('input_example.txt') as fd:
with open('input.txt') as fd:
    numbers = fd.readline().rstrip().split(',')

    for line in fd:
        if line.rstrip():
            tmp_card.append(line.rstrip().split())
        else:
            if tmp_card:
                cards.append(tmp_card)
            tmp_card = []

cards.append(tmp_card)
found = False
total = 0
last_winner = []
last_winning_number = 0

for num in range(5,len(numbers)+1):
    curr_card = None
    print('----- called new number -------')
    sorted_nums = numbers[:num]
    print(sorted_nums)
    print(f"number of cards left: {len(cards)}")

    is_bingo = False

    for card in cards:
        #  print('new card')
        #  pprint(card)
        if check_for_bingo(numbers[:num], card):
            print('BINGO!')
            pprint(card)
            last_winner=card.copy()
            last_winning_number = int(num) - 1
            is_bingo = True
            break

    if is_bingo == True:
        print("REMOVING")
        #  pprint(card)
        cards.remove(last_winner)
        #  found = False

        #  print("FOUND")
        #  for line in card:
            #  print(f"LINE: {line}")
            #  total += sum( [int(i) for i in set(line).difference(numbers[:num])] )
        #  print(total)
        #  print(f"number: {numbers[num-1]}")
        #  print(f"{total * int(numbers[num-1])}")
        #  exit()

#  if len(cards) ==  1:
    #  print("THE LAST ONE")
    #  print(cards)

print('calculate score')
print('winner:')
pprint(last_winner)
print(last_winning_number)
for line in last_winner:
    total += sum( [int(i) for i in set(line).difference(numbers[:last_winning_number] )])
print(total)
print(f"number: {numbers[last_winning_number]}")
print(f"{total * int(numbers[last_winning_number])}")

#  pprint(cards)
#  print(numbers[0:5])

