num = int(input("enter a range for printing fibonacci sequence : "))
a = 0
b = 1
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1): 
        c = a + b
        a = b 
        b = c
        print(c)        