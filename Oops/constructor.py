class Dog:
    count=0

    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        Dog.count=Dog.count+1

    def about(self):
        print("Name:%s"%(self.name))
        print("Age:",self.age)
        print("color:",self.color)

dog1=Dog("Jimmy",5,"White")
dog2=Dog("Pluto",6,"Gray")

dog1.about()
dog2.about()
print("No of objects:",Dog.count)