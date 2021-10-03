# Python program to swap two element in a list
l=[23,54,58,24,75]
n1=int(input("enter first number to swap: "))
n2=int(input("enter second number to swap: "))
i1=l.index(n1)
i2=l.index(n2)
temp=l[i1]
l[i1]=l[i2]
l[i2]=temp
print(l)

# # 2nd Method
l[i1],l[i2]=l[i2],l[i1]
print(l)



# Not Worked Methods
# 3rd method
# i1=l.index(n1)
# i2=l.index(n2)
# temp=l.pop(i1) #length of the list will change
# temp2=l.pop(i2)
# l.insert(i1,temp2)
# l.insert(i2, temp)
# print(l)

# l=[23,54,58,24,75]
# temp=l[l.index(n1)]
# l[l.index(n1)]=l[l.index(n2)]
# l[l.index(n2)]=temp
# print(l)