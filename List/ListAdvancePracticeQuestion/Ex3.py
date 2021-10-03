# Extract elements with frequency greater than k
L=[1,2,2,5,4,1,5,4,3,3,5,4]
L1=[]
for i in L:
    if L.count(i)>2:
        if i not in L1:
            L1.append(i)
print(L1)