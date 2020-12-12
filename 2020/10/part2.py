import sys

adapters=[]
arrangements={ 0: {} }
total_configs=0
total_calls=0

def do_adapters( arr ):

    global total_calls

    total_calls+=1
    print('total: {}'.format(total_calls))

    global total_configs

    for x in arr.keys():
        for y in [ 1, 2, 3 ]:
            if (x+y) in adapters:
                arr[x][x+y] = {}
        if arr[x] == {}:
            total_configs+=1
        else:
            do_adapters(arr[x])

    total_calls-=1

for line in sys.stdin:
    adapters.append(int(line.strip()))
    
do_adapters( arrangements )
print(total_configs)
