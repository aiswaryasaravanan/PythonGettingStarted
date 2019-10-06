class Dog:
    count=0

    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        Dog.count=Dog.count+1

dog=Dog("Pluto",5,"Golden")

print(getattr(dog,"name"))
print(setattr(dog,"name","Jimmy"))
print(getattr(dog,"name"))
print(hasattr(dog,"count"))
print(hasattr(dog,"name"))
# delattr(dog,"name")

print(dog.__dict__)
print(dog.__doc__)
print(dog.__module__)
# print(dog.__bases__)