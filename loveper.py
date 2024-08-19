

print("\nwelcome to lovepercentage where you can find persentage of your love\n ")


ask = str(input("Enter your gender \n M for Male \n F for Female \n :").capitalize())

username = str(input("enter your name : ").capitalize())

if ask == "M":
    partner_name = str(input("Enter your Girlfriend's Name : ").capitalize())
elif ask == "F":
    partner_name = str(input("Enter your Boyfried's Name : ").capitalize())
else:
    print("Invalid gender input.")
    exit()
    
if not partner_name:
    print("Partner's name cannot be empty.")
    exit()

print(f"your name is {username} and your partener name is {partner_name}")


x = int(ord(username[0]))+ int(ord(username[1]))+int(ord(ask[0]))
y = int(ord(partner_name[0])) + int(ord(partner_name[1]))+int(ord(ask[0]))
z = x * y/0.5

percentage = z % 100

print(f"hey {username} yous and {partner_name}'s love percentage is : {percentage}% ")