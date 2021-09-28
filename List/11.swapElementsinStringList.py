L=['We', "don't", 'need', 'permission', 'to' 'dance']
f=[]
for i in L:
    M =  i.replace('e','E').replace('o','O')
    f.append(M)
print(f)
