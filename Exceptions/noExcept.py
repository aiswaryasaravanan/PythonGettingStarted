a=int(input("Enter A:"))
b=int(input("Enter B:"))

try:
    c=a/b
    print(c)
except:
    print("Divide by zero error")