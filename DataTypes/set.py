set1 = {1, 2, 3, 4}
# no indexing
# no order
# no duplicate
# immutable

for i in set1:
    print(i)

# list to set
list1 = [1, 2, 3, 4, 5, 6]
set2 = set(list1)
print(set2)

set2.add(7)
print(set2)
set2.update([8, 9, 10])
print(set2)
set2.discard(10)
print(set2)

print(set1 | set2)
print(set1.union(set2))
print(set1 & set2)
print(set1.intersection(set2))
print(set1-set2)
print(set1.intersection_update(set2))
print(set1 > set2)
print(set1 < set2)
print(set1 == set2)


# frozen set
# immutable cant add or remove
# store dict keys

Dictionary = {"Name": "John", "Country": "USA", "ID": 101}
print(type(Dictionary))
# Frozenset will contain the keys of the dictionary
Frozenset = frozenset(Dictionary)
print(type(Frozenset))
for i in Frozenset:
    print(i)
