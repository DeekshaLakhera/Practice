# program to retain records with N occurances of K
L=[1,2,3,3,3,4,4,2,4,5,1,6]
N=int(input("Enter number of occurance: "))
# K=int(input("enter item to check: "))
for i in L:
    if L.count(i)==N:
        print(f'{i} in index {L.index(i)} is having {N} occurances')