# replace index elements with elements in other list
L=[27,21,16,23,26,4,2]
L1=[4,9,18,12,13,30,1]
for i in range(len(L)):
    temp=L[i]
    L[i]=L1[i]
    L1[i]=temp
print(L)
print(L1)