# count unique value in a list
from typing import Counter


L=[45,85,77,65,45,85]
count=0
L1=[]
for i in L:
    if i not in L1:
        count+=1
        L1.append(i)
print(count)

# from collections import Counter

# i=Counter(L).keys()
# print(len(i))
L=[1,2,1,2,2,3,4,2,5]
# print(len(Counter(L).keys()))
# S='Deeksha Lakhera'
# print(Counter(S))