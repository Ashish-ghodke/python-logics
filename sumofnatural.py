num = int(input("enter a number : "))
if num < 0: 
    print("enter positive number ")
else : 
    sum = 0
    while num>0:
        sum += num
        num -= 1
    print(sum)