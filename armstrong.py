num = int(input("enter a number to check its amstrong number or not : "))
sum = 0 
temp = num
while temp > 0:
    digit = temp%10
    cube = digit**3
    sum = sum + cube 
    temp //= 10
if sum == num:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number ")