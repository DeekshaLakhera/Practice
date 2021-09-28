
L=['B',27,'W',21,'BW',12]
d={}
m=list(range(0,len(L)-1,2))
for i in m:
	d[L[i]]=L[i+1]
print(d)
