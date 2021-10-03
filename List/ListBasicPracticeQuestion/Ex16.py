# program to find larest number in a List
L=[27,21,30,27,12,13,12,27]
# 1st Method
# print(max(L))


# 2nd Method but changing the List
# for i in range(len(L)-1):
#     if L[i]>L[i+1]:
#         temp=L[i]
#         L[i+1]=temp
# print("Largest Number in the list : ",temp)

#3rd method
L.sort()
print(L)
print(L[len(L)-1])

