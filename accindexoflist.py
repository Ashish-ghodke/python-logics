# PROGRAM TO ACCESSING INDEX OF LIST USING FOR LOOP

lst = [1,3,4,5,6,7,8,]
for index , value in enumerate(lst):
    print("at index",index," we have ", value)
    
# solution without enumerate 

for index in range(len(lst)):
    value = lst[index]
    print("at index",index," we have ", value)