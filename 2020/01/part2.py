#  --- Day 1: Part Two ---

#  The Elves in accounting are thankful for your help; one of them even offers
#  you a starfish coin they had left over from a past vacation. They offer you
#  a second one if you can find three numbers in your expense report that meet
#  the same criteria.

#  Using the above example again, the three entries that sum to 2020 are 979,
#  366, and 675. Multiplying them together produces the answer, 241861950.

#  In your expense report, what is the product of the three entries that sum to
#  2020?

entries = []

with open('input.txt') as fd:
    for row in fd:
        entries.append( int(row.rstrip('\n')) )

for entry_index, entry in enumerate(entries):
    entry_removed = entries
    del entry_removed[entry_index]

    for entry_two in entry_removed:
        try:
            match = entries.index( 2020 - entry - entry_two )
            print('{} + {} + {} = {}'.format( entry, entry_two, entries[match], entry + entry_two + entries[match]))
            print('{} * {} * {} = {}'.format( entry, entry_two, entries[match], entry * entry_two * entries[match]))
            break
        except ValueError:
            next
