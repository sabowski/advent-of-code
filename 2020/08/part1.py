import sys

code=[]
for line in sys.stdin:
    x = line.strip().split(' ')
    code.append(x)

pointer=0
no_repeat=True
accumulator=0

while no_repeat:

    if len(code[pointer]) == 3:
        break

    instruction=code[pointer][0]

    if instruction == 'acc':
        accumulator+=int(code[pointer][1])
        code[pointer].append('x')
        pointer+=1
    elif instruction == 'jmp':
        code[pointer].append('x')
        pointer+=int(code[pointer][1])
    elif instruction == 'nop':
        code[pointer].append('x')
        pointer+=1

print(accumulator)
