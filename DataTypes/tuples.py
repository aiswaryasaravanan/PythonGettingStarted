# tuples
# Indexing
# can hae duplicates
# immutable
# ordered

tuple1 = ("Aishu", "006", "Aishu")
tuple2 = ('Swathi', "007", "Aishu")

print(tuple1)
print(tuple2)

print(tuple1+tuple2)
print(tuple1*2)

print(tuple1[0])
print(tuple2[0:])
print(tuple1[0:2])
print(tuple1[0:5])  # out of range

print(tuple1+tuple(tuple2[0]))
print(tuple1+tuple([tuple2[0]]))

print(min(tuple1))
print(max(tuple2))
print(len(tuple1))
# print(cmp(tuple1, tuple2))

del tuple2

tuple3 = tuple(["Aishu", "Ransom"])
print(tuple3)
# tuple1[0] = "Aishu Saravanan" #cant reassign
# del tuple2[0]     #TypeError: 'tuple' object doesn't support item deletion
