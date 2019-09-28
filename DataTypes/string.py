str = "Aishu"
print(type(str))

# TypeError: 'str' object does not support item assignment
# str[0] = "a"
# print(str)

str = "aishu Saravanan"
print(str)

for i in str:
    print(i, end=" ")

# to print raw string...as it is
print(r'C://directory')

print(str.capitalize())
print(str.casefold())
print("a".center(5))
print(str.count("a", 0, 10))
print(str.find("u"))
print(str.swapcase())
print(str.capitalize())
print(str)
print(str.swapcase())
print("a".zfill(4))  # left zero padding


if str.isidentifier():
    print("yes")
else:
    print("no")


if "  ".isspace():
    print("yes")
else:
    print("no")
