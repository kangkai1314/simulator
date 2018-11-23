import itertools


for i in [12,13,14]:
    for j in [1,2,3]:
        print i,j

for i in itertools.product([12,13,14]):
    for j in itertools.product([1,2,3]):
        print i,j

