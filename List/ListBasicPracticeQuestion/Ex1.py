# 1. Python program to interchange first and last element in a list.
l=[23,54,58,24,75]
# 1st Method
temp=l[0]
l[0]=l[len(l)-1]   ##l[0]=l[-1]
l[len(l)-1]=temp   ##l[-1]=temp
print(l)

# #2nd Method
l[0],l[len(l)-1]=l[len(l)-1],l[0]

## 3rd Method
l=[23,54,58,24,75]
l1=l.pop(0)
l2=l.pop(-1)
l.insert(0,l2)
l.append(l1)
print(l)

