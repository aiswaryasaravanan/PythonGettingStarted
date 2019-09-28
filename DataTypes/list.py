# list

# can have duplicates
# ordered
# mutable
# indexed

list1 = [1, "a", "Aishu", 1.1]
list2 = ["Aishu"]

print(list2*2)
print(list1+list2)
print(len(list1))
print(1 in list1)

for i in list1:
    print(i, end=" ")

list3 = list(list1[0:2])
print(list3)

list4 = []
for i in range(0, 5):
    list4.append(input("Enter list item"))
print(list4)

list1.remove(1.1)
print(list1)

print(min(list4))
print(max(list4))
print(len(list4))
print(list("AishuSaravanan"))
print(list4.sort())

# print(list1.pop(list1[-1]))

list5 = [1, 2, 3, 4, 5]
list5.remove(3)
list5.insert(4, 3)
print(list5)
list5[3] = 3  # can be reassigned
print(list5)
