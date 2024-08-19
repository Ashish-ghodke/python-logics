#  FIBONACHI SEQUANCE USING RECURSION 

def fibonachi(n):
    if n <= 1:
        return n
    else:
        return fibonachi(n-1 ) + fibonachi(n-2)

n = int(input("ENTER A NUMBER HERE : "))

if n <=0 :
    print("enter a positive number")
    
else: 
    print("fibobacci sequence")
    for i in range(n):
        print(fibonachi(i))