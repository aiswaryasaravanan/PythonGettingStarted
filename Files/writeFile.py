# Writing to files

fileobj = open("bFile.txt", "w+")
fileobj.write("I am talking to you only\n")

fileobj.write("Looking good:)")

# With keyword

# with open("bFile.txt", "r") as fileobj1:
#     content = fileobj1.read()
#     print(content)
