print('*** Fun with Drawing ***')
a = int(input('Enter input : '))
ra = ((a*2)-1)+((a*2)-2)
count = 0
cRow = 0
for x in range(0,ra):
    for i in range(0,ra):
        count+=1
        if count == 1 or count == ra:
            print('#', end='')
        elif cRow%2 != 0:
            print('.', end='')
        else:
            print('#', end='')
    print()
    count=0
    cRow+=1
