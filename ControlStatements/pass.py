# pass
list = [1, 2, 3, 4, 5]
flag = 0
for i in list:
    print("Current element:", i, end=" ")
    if i == 3:
        pass
        print("We are inside pass block")
        flag = 1
    if flag == 1:
        print("Came out of pass")
        flag = 0
