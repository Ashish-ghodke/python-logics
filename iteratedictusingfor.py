# PROGRAM TO ITERATE OVER DICTIONATIES USING FOR LOOP 

D = {1:"ashish",2:"nominath",
     3: "pushkar", 4:"sarthak",
     5: "dhiraj", 6: "vivek",
     7: "sarika", 8:"santoshi",}

print(D)
print(D[3])
print(D[1])
for i in range(len(D)):
     print("on index",i , " we have " ,D[i+1])