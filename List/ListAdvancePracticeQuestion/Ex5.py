# Check elements who occure consecutively 3 times
L=[1,2,2,3,3,3,4,4,4,5,5,5,6]
# first Method
for i in range(len(L)-1):
    if L[i]==L[i+1]:
        if L[i+1]==L[i+2]:
            print(f"{L[i]} exist consecutively 3 times")

# Second Method
for i in range(len(L)):
    if L.count(L[i])==3:
        if L[i]==L[i+1]:
            if L[i]==L[i+2]:
                count=3
                print(f"{L[i]} exist consecutively 3 times")