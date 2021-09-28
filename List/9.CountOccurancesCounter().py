from collections import Counter
L=[1,2,5,1,4,2,3,5,4,6]
m=Counter(L)
print(m)


##first element from each nested list
k=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
for i in k:
    l.append(i[0])
print(l)
