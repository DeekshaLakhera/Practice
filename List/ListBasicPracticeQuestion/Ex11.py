# Count occurance of an element in a List
from collections import Counter #to use Counter Function

L=[27,21,30,27,12,13,12,27]
n = int(input("enter an element whose Occurance you want to Know: "))
# print(L.count(n))

count=0
for i in L:
    if i==n:
        count+=1
if count!=0:
    print(f"Occurance of {n} in List: ",count)
else:
    print("Element Doesn't Exist")

# New Method but for this method we have to import Counter from collection library
cnt=Counter(L)
print(f"Occurance of {n} in {L} is: ",cnt[n])