l=[10,20,30,30,30,20,10,10,40]
lc=l.copy()
for i in l:
    for j in range(len(lc)):
        if j<len(l)-1:
            if l[j]==l[j+1]:
                print(l)
                del l[j]
print(l)

##for i in range(len(lc)):
##    if i<len(l)-1:
##        if l[i]==l[i+1]:
##            del l[i]
##print(l)
