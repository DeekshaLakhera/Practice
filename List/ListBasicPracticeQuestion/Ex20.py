L=[27,21,30,27,9,12,13,12,27]
L1=[]
countE=0
countO=0
for i in L:
    if i%2==0:
        countE+=1
    elif i%2!=0:
        countO+=1
        
print("Numbers of Even Numbers in The List L: ",countE)
print("Numbers of Odd Numbers in The List L: ",countO)