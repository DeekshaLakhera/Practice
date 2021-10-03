# Reversing a list
L=[27,21,30,13,12]
# First Menthod
# L.reverse()
# print(L)

# 2nd Method
# print(L[::-1])

##3rd method
print(list(reversed(L)))

# using an empty list
# 4th Method
# L1 =[]
# for i in range(len(L)-1,-1,-1):
#     L1.append(L[i])
# print(L1)

# 5th Meethod
L1=[]
for i in range(len(L)):
    popped=L.pop()
    L1.append(popped)
print(L1)

# 5th Method
# for i in range(len(L)):
#     L[i]=L[(len(L)-1)-i]
# print(L)
