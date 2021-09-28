def remove_neg(a):
	if a>=0:
		return True
	else:
		return False
L=[-12,-55,12,85,-55,98]
k=[a for a in filter(remove_neg,L)]
print(k)
