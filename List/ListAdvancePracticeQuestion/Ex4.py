# check if elements of list are in range or not
L=[45,85,24,55,65,25]
n=int(input("Enter the range of the elements: "))
for i in range(len(L)):
    if L[i]>n:
        print(f"Element {L[i]} which is in position {i} is not in range")
       