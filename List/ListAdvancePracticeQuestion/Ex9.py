# Strongest neighbour 
L=[27,21,16,23,26,4,2]
for i in range(1,len(L)-1):
    print(f"Strongest neighbour of {L[0]} is: ", L[1])
    if L[i-1]>L[i+1]:
        print(f"Strongest neighbour of {L[i]} is: ", L[i-1])
    else:
        print(f"Strongest neighbour of {L[i]} is: ", L[i+1])
print(f"Strongest neighbour of {L[len(L)-1]} is: ", L[len(L)-2])
