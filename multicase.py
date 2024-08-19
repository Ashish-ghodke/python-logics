# write a program using function to find greatest of three numbers 
def greatest(a, b, c):
    if a == b == c:
        print("All entered numbers are equal")
    elif a == b and a > c:
        print(f"{a} and {b} are equal and {a} is greater than {c}")
    elif a == c and a > b:
        print(f"{a} and {c} are equal and {a} is greater than {b}")
    elif b == c and b > a:
        print(f"{b} and {c} are equal and {b} is greater than {a}")
    elif a > b and a > c:
        print(f"{a} is greater than {b} and {c}")
    elif b > a and b > c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())
greatest(num1, num2, num3)

print("End of program")
