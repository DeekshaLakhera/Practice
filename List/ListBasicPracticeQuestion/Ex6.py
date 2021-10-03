# Minimum of Two Numbers in Python
n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
if n1<n2:
    print(f"{n1} is minimum.")
else:
    print(f"{n2} is minimum.")

print(min(n1,n2))
print(f"minimum of {n1} and {n2} is : ",n1 if n1<n2 else n2)