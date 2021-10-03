# #Sum Of the Number Digits of List
L=[27,21,30,13,12]
L1=[]
for i in L:
    sum=0
    for j in str(i):
        sum+=int(j)
    L1.append(sum)
print(L1)


# Mechanism
# l=21
# for j in str(l):
#     print(int(j))
# for j in 'hello':
#     print(j)


# L=['B', 27, 'W', 21, 'V', 30, 'BW', 2721 ]
# sum=0
# for i in L:
#     if type(i)==int:
#         sum+=i
# print(sum)