##l='Apple'
l='axxcxxxxcd'
p=list(l)
for i in range(len(p)-1):
    for j in range(len(p)-1):
        if p[i]==p[i+1]:
            p[i+1]='?'
k="".join(p)
print(k)
##l='axxcxxxxcd'
##p=list(l)
##m=[]
##for i in range(len(p)):
##    if p[i]!=p[i+1]:
##        m.append(p[i])
##    if p[i]==p[i+1]:
##        p[i+1]='?'
##        m.append(p[i+1])
##k="".join(m)
##print(k)










##for i in range(len(l)-1):
##    if l[i]==l[i+1]:
##        print(l[i],l[i+1])
##        m=l.replace(l[i+1],'?')
##print(m)
##o=''
##for i in range(len(l)-1):
##    if l[i]!=l[i+1]:
##        o+=l[i]
##    else:
##        o+=l[i]
##        o+='?'
##print(o)
    
