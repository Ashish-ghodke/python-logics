# program to merge two dictionaries 

# solutiohn 1 using bar operator 

dict1 = {"ashish":89 , "nominath": 99}
dict2 = {"pushkar":94 , "sarthak": 79}

print(dict1|dict2)

# soution number two ** operator 


dict1 = {"ashish":89 , "nominath": 99}
dict2 = {"pushkar":94 , "sarthak": 79}

print({**dict1,**dict2})

# solution number three using copy and update method 

dict1 = {"ashish":89 , "nominath": 99}
dict2 = {"pushkar":94 , "sarthak": 79}

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)