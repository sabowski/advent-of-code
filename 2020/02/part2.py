#  --- Day 2: Part Two ---

#  While it appears you validated the passwords correctly, they don't seem to
#  be what the Official Toboggan Corporate Authentication System is expecting.

#  The shopkeeper suddenly realizes that he just accidentally explained the
#  password policy rules from his old job at the sled rental place down the
#  street! The Official Toboggan Corporate Policy actually works a little
#  differently.

#  Each policy actually describes two positions in the password, where 1 means
#  the first character, 2 means the second character, and so on. (Be careful;
#  Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
#  these positions must contain the given letter. Other occurrences of the
#  letter are irrelevant for the purposes of policy enforcement.

#  Given the same example list from above:

    #  1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    #  1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    #  2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

#  How many passwords are valid according to the new interpretation of the
#  policies?

import re

valid_passwords = 0

def check_position(text, letter, pos):
    if text[int(pos)-1] == letter:
        return True
    else:
        return False

with open('input.txt') as fd:
    for row in fd:
        (pos1, pos2, letter, password) = re.match(r'^(\d+)-(\d+) (.): (.*)$',row.rstrip('\n')).groups()

        if check_position(password, letter, pos1) ^ check_position(password, letter, pos2) == True:
            valid_passwords+=1

print('number of valid passwords: {}'.format(valid_passwords))
