# mutable -> call by reference
# immutable -> call by value


def add(a, b):
    print(a+b)


add(1, 2)

# call by reference


def immutable(s):
    s = "Aishu Saravanan"
    print("Inside function", s)


s = "Aishu"
print("Before calling..", s)
immutable(s)
print("Ouside function...After calling", s)


# call by value
def mutable(list1):
    list1[0] = "Aishu Saravanan"
    list1[1] = "RamBabu Saravanan"


list1 = ["Aishu", "RamBabu"]
print("Before calling", list1)
mutable(list1)
print("After calling", list1)
