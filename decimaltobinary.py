# PROGRAM TO DECIMAL NUMBER TO BINARY,OCTAL AND HEXADECIMAL NUMBERS

class Numbersystem:
    def __init__(self,num):
        self.num = num
    def binary(num):
        print(f"{num} is ",bin(num),"in binary number system ")
    def octal(num):
        print(f"{num} is ",oct(num),"in octal number system")
    def hexadecimal(num):
        print(f"{num} is ",hex(num),"in hexadecimal number system")

N1 = Numbersystem

num = int(input("enter a Decimal number : "))
choice = int(input("press 1 to convert in binary number \npress 2 for convert in octal number \npress 3 for convert in hexadecimal number : "))
if choice in {1,2,3}:
    match choice:
        case 1:
            N1.binary(num)
        case 2:
            N1.octal(num)
        case 3:
            N1.hexadecimal(num)
else: print("enter correct choice")