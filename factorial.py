import math
def factorial(x):
    if x < 0 :
        return "factorial of entered number is does not exist"
    elif x == 1 or x == 0 :
        return 1
    else :
        return x * factorial(x-1)

print(factorial(4)) 
print(math.factorial(4))