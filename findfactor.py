# program to find the facgtors of a number
num = int(input("enter a number to find to factor : "))
for i in range(1 , num+1):
    if num % i == 0:
        print(i)
    