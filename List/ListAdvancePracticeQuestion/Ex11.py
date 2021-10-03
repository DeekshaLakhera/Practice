##print all possible combination from the three digit
##L=[1,2,3]
##for i in L:
##    for j in L:
##        for k in L:
##            if i !=j and j!=k and k!=i:
##                print(i , j , k)

L=[1,2,3]
L1=[]
for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            if i !=j and j!=k and k!=i:
                t=(L[i], L[j] , L[k])
                L1.append(t)
print(L1)

from itertools import permutations
combination=permutations([1,2,3],3)
for item in combination:
    print(item)
                    

