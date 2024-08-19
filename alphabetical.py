# PROGRAM TO SORT WORLD IN ALPHABETICAL ORDER 
str = str(input(" ENTER STRING HERE : "))
print(f"original string is : {str}")
a = str.split()
for i in range(len(a)):
    a[i] = a[i].lower()
a.sort()
print(a)