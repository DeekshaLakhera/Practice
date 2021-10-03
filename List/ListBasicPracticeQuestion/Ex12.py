# Sum and Average of the list
L=[27,21,30,27,12,13,12,27]
# 1st method
S=0
for i in L:
    S+=i
print("Sum of the List: ",S)
Av=S/len(L)
print("Average of the List: ",Av)

## 2nd Method
print(f"Sum of the List {L}: ", sum(L))
print(f"Average of the list {L}: ", sum(L)/len(L))