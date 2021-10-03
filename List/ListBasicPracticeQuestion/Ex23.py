# count positive and negative numbers in a list
L=[-2, 8,-32, -56, 45, 58,-95]
countP=0
countN=0
for i in L:
    if i>=0:
        countP+=1
    elif i<0:
        countN+=1
print("total number of Positive Numbers in the list: ",countP)
print("total number of Negative Numbers in the list: ",countN)