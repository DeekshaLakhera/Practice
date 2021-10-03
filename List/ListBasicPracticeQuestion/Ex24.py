# remove multiple elements from a list
L=[27,21,30,27,9,12,13,12,27]

L1=[]
for i in L:
    if i not in L1:
        L1.append(i)
print(L1)


# for i in L:
#     j=i
#     for j in range(L.index(j)+1,len(L)):
#         if j in L:
#             L.remove(j)
#     else:
#         pass
# print(L)


# for i in L:
#     for j in L:
#         if i == j:
#             L.remove(L[j])
# print(L)



# for i in L:
#     # print(i)
#     for j in L:
#         # print(j)
#         if i==j:
#             L.remove(j)
#     if j not in L:
#         # L.append(j)
#         L.insert(L.index(j),j)
# print(L)