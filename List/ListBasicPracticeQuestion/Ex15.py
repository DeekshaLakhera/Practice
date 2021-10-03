# smallest number in a List
L=[27,21,30,27,9,12,13,12,27]
# 1st Method
# print(min(L))

# 2nd Method
for i in range(len(L)-1):
    if L[i]<L[i+1]:
        temp=L[i]
        L[i+1]=temp
print("Smallest number in the List: ",temp)

#3rd method
# L.sort()
# print(L)
# print(L[0])