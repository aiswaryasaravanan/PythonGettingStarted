a=int(input("Enter A:"))
b=int(input("Enter B:"))

try:
    c=a/b
    print(c)
except Exception:
    print("Divide by zero error")
finally:
    print("Thanks...See you soon:)")