class Dog:
    name="pluto"
    age=5
    color="white"
    def convo(self):
        print("Barking")

    def about(self):
        print("Name:%s\nAge:%d\nColor:%s"%(self.name,self.age,self.color))

class Chair:
    legs=4
    material="furniture"
    weight=3.5

    def about(self):
        print("I am made of %s with %f kg having %d legs"%(self.material,self.weight,self.legs))

dog=Dog()
chair=Chair()

dog.convo()
dog.about()
chair.about()