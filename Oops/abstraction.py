# __variableName for achieving data abstraction
# if so... cant access from outside the class using object

class A:
    __a=5
    def __init__(self,b):
        self.b=b

    def fun(self):
        print(self.b)

obj=A(2)
obj.fun()
print(obj.b)
# print(obj.a)      #cant
# print(A.a)