# remove empty tuples from list
L=[25,(),58,75,(),(5,4,3)]
for i in L:
    if i==():
        L.remove(i)
print(L)