# Maximum of Two Numbers in Python
n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
if n1>n2:
    print(f"{n1} is maximum.")
else:
    print(f"{n2} is maximum.")

print(max(n1,n2))
# # new
print(n1 if n1>n2 else n2 )
