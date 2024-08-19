# remove punctuation from string 
a = """!@#$?./,%^&*()[]|""" 
str = str(input("ENTER STRING HERE : "))
print(f"original string : {str}")
empt = ""

for i in str :
    if i not in a: 
        empt += i 
print(empt)