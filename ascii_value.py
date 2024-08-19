# program to find ASCII value of character 
# ASCII = American Standard Code for Information Interchange
# using inbuilt function ord()
for i in range(1,26):
    char = str(input("enter letter : "))    
    print("the ASCII value of ",char,"is",ord(char))