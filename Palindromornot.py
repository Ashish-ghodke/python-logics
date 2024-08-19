# PROGRAM TO CHECK ENTERED STIRNG IS PALINDEOME OR NOT 
# IN PALINDROM WE JUST SIMPLY WRITE STRING IN REVERSE ORDER AND CHECK IS LOOK LIKE ORIGINAL STRING OR NOT
# EXAMPLE OF PALINDROME 
# WOW = WOW , MADAM = MADAM ,

string = str(input("enter string here : "))



reverse = string[::-1]
if reverse == string:
    print("its palendrom")
else:
    print("its not palendrom ")