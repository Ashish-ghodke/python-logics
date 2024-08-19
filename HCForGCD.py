# program to find HCF or GCD
# HCF = Highest Commen Factor

def calculate_hcf(x,y):
        if x > y:
            smaller = y
        else : 
            smaller = x
        for i in range (1,smaller+1):
            if (x%i == 0) and (y % i == 0):
                hcf = i 
        return hcf
print("the hcf of the given two numbers is ",calculate_hcf(12,30))