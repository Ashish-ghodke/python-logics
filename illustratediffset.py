# PROGRAM TO ILLUSTRATE DIFFERENT SET OPERATIONS 
# UNION ,INTERSECTION ,DIFFERENCE , SYMMETRIC DIFFERENCE 

A = {1,2,3,4,5}
B = {2,4,6,8,10}
print(f"set A : {A}")
print(f"set B : {B}")

print("THE UNION OF SET A AND B : ",A | B)
print("THE INTERESECTION OF SET A AND B : ",A&B)
print("THE DIFFERENCE OF SET A AND B : ",A - B)
print("THE SYMETRIC DIFFERENCE IS :", A ^ B)