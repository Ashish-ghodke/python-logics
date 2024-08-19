# anominous fuction = Lamda function 
A = int(input("enter the numbers of terms : "))

result = list(map(lambda x : 2 ** x , range(A+ 1)))


for i in range(0,A+1):
    print('the value of 2 raised to power',i,"is",result[i])