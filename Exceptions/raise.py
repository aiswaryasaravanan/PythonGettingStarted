age=int(input("Enter Age:"))

try:
    if age<18 :
        raise ValueError
    else:
        print("Your age is valid")
except ValueError:
    print("Age is invalid")