import sys
import copy


def run_program(run_code):

    pointer=0
    accumulator=0
    #  clean_exit=False

    while True:

        if len(run_code) == pointer:
            # we are at the end
            #  clean_exit=True
            print('it worked')
            print(accumulator)
            return True
            #  break

        if len(run_code[pointer]) == 3:
            # we are repeating
            print("repeat baby!")
            return False

        instruction=run_code[pointer][0]

        if instruction == 'acc':
            accumulator+=int(run_code[pointer][1])
            run_code[pointer].append('x')
            pointer+=1
        elif instruction == 'jmp':
            run_code[pointer].append('x')
            pointer+=int(run_code[pointer][1])
        elif instruction == 'nop':
            run_code[pointer].append('x')
            pointer+=1

code=[]
for line in sys.stdin:
    x = line.strip().split(' ')
    code.append(x)

#  print(code)

for index, step in enumerate(code):

    print(step)

    if step[0] == 'acc':
        print('its acc')
        continue

    if step[0] == 'jmp':
        print('its jmp')
        code_new = copy.deepcopy(code)
        code_new[index][0] = 'nop'
    elif step[0] == 'nop':
        print('its nop')
        code_new = copy.deepcopy(code)
        code_new[index][0] = 'jmp'


    if run_program(code_new):
        exit()
