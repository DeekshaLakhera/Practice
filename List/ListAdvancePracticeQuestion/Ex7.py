# all possible compination of two lists
# L=[27,21,16,23,26,4,2]
# L1=[4,9,27,2,16,30,1]
L=[27,21,12]
L1=[30,1]
L3=[]
Lf=[]
Ls=[]
L4=[]
L5=[]
for i in L:
    L3.append(i)
    for j in L1:
        if j not in L3:
            L3.append(j)
            Lf=L3.copy()
            L4.append(Lf)
    L3.clear()
print(L4)
for i in L1:
    L3.append(i)
    for j in L:
        if j not in L3:
            L3.append(j)
            Ls=L3.copy()
            # print(L3)
            L5.append(Ls)
    L3.clear()
print(L5)



##CLASS

##unique combination
from itertools import permutations
com=permutations(L,len(L1))
for c in com:
    print(c)
##zip function merging one one combination L[0]-L1[0],L[1]-L1[1],L[2]-l1[2]
L=['b','v','t']
L1=['w','j','m']
for item in zip(L,L1):
    print(item)



    
from itertools import permutations
l1=['x','y','z','l']
l2=[1,4,9]
lc=[]
com=permutations(l1,len(l2))
for c in com:
    zipped=zip(c,l2)
    lc.append(list(zipped))
print(lc)
