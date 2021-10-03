# Different Ways to clear a list in Python
L=[54,85,66,25,45]
# 1st Method
# L.clear()
# print(L)

# 2nd Method
for i in range(len(L)):
    L.pop()
print(L)

# 3rd Method
# for i in range(len(L)-1,-1,-1):
#     L.remove(L[i])
# print(L)

# 4th method
# del L[:]

# print(L)
