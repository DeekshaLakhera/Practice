# # List product excluding duplicates
L=[45,85,77,65,45,85]
L1=[]
for i in L:
    if L.count(i)>1:
        L1.append(i)
mul=1
L1=list((set(L)-set(L1)))
print("After removing Duplicates from the list: ",L1)
for i in L1:
    mul*=i
print("Multiplication of list product excluding duplicates: ",mul)



# L=[45,85,77,65,45,85]
# L1=[]
# mul=1
# for i in L:
#     if i not in L1:
#         L1.append(i)
#         mul*=i
# print(mul)