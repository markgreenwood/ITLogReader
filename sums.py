import random

a = [ random.randint(0,10) for i in range(30) ]

ht = {}

for i in range(len(a)):
    if a[i] in ht.keys():
        ht[a[i]].append(i)
    else:
        ht[a[i]] = [ i, ]