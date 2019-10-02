import operation;   #import
from xoperation import exponential;     #from import
# import operation as op;     #renaming module

a=int(input("Enter A:"))
b=int(input("Enter B:"))

print("Addition:",operation.addition(a,b))
print("Subtraction:",operation.subtraction(a,b))
print("Multiplication:",operation.multiplication(a,b))
print("Division:",operation.division(a,b))

print("Exponential:",exponential(a,b))

print(dir(operation))