#remove all the occurance of an element from a list
L=[1,2,3,3,3,4,4,4,5,5,5,6]
L1=[]
L2=L.copy()
n=int(input("enter number who you want to remove from the list : "))

for i in range(len(L)):
    if (L[i]==n):
        L2.remove(n)
L=L2
print(L) 

   
# for i in range(len(L)-1,-1,-1): #Run
#     if L[i]==n:
#         del L[i]
# print(L)    

# while n in L: #Run
#     L.remove(n)
# print(L)

# for i in L:
#     if L.count(i)>1:
#         e=i
#         L.remove(e)
# print(L)




# for i in L:
#     L1.append(i)
#     for j in range(i+1,len(L)):
#         if i==L[j] or i not in L1:
#             L1.append(i)
#             # L.remove(i)
# print(L1)
