# PROGRAM TO FIND NUMBERS DIVISIBLE BY ANOTHER NUMBER 
# solution 1 using for loop 

for i in range(1,101):
    if i % 13 == 0 :
        print(i)

#solution 2 using lamda function and filter()

lst = [39,48,26,98,33,67,87] 
result = list(filter(lambda x : x % 13 == 0, lst))
print(f"the number divisible by 13 is : {result}")

