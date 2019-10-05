

    # ZeroDivisionError: Occurs when a number is divided by zero.
    # NameError: It occurs when a name is not found. It may be local or global.
    # IndentationError: If incorrect indentation is given.
    # IOError: It occurs when Input Output operation fails.
    # EOFError: It occurs when the end of the file is reached, and yet operations are being performed.


a=int(input("Enter A:"))
b=int(input("Enter B:"))

try:
    c=a/b
    print(c)
except Exception:
    print("Divide by zero error")