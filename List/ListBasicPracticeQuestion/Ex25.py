# program to print duplicate from a list of integers

L=[27,21,30,27,9,12,13,12,27]
#1st method
L1 =[]
for i in L:
    if i not in L1:
        if L.count(i)>1:
            L1.append(i)
print(L1)

# 2nd method
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
            print(L[i])
            
        