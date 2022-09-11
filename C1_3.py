from itertools import permutations
from posixpath import split
print('*** Fun with permute ***')
a = input('input : ')
b = a.split(',')
i = 0
c = permutations(b)
for x in c:
    print(x,sep=(''))