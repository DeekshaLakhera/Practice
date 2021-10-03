# print odd numbers in a list
L=[27,21,30,27,9,12,13,12,27]
L1=[]
for i in L:
    if i%2!=0:
        L1.append(i)
print("Odd Numbers in The List L: ",L1)
