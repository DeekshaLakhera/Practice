# Ways to check if element exixt in list
L=[24,58,12,65]
n=int(input("Enter Element to check in List: "))
# 1st method
if (n in L):
    print(f"{n} is exist in the list")
    
else:
    print(f"{n} is not exist in the list")

#2nd Method
if L.count(n)>0:
    print(f"{n} exist")

    