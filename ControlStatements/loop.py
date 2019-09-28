for i in range(0, 10):
    print(i, end=' ')

list1 = ["Aishu", 6, "CSE"]

for i in list1:
    print(i)

# printing pattern

for i in range(0, 10):
    for j in range(0, i):
        print("*", end=' ')
    else:  # else with for
        print(" ")


i = 5
while i >= 0:
    print(i, end=" ")
    i = i-1
else:
    print("less than zero")
