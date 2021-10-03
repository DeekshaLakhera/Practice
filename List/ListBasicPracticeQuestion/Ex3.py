# Python Program to Swap elements in String List
l=["B","W","V","J","K"]
n1=input("enter first String to swap: ")
n2=input("enter second String to swap: ")
i1=l.index(n1)
i2=l.index(n2)
temp=l[i1]
l[i1]=l[i2]
l[i2]=temp
print(l)

#2nd Method
l[i1],l[i2]=l[i2],l[i1]
print(l)
