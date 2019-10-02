fileobj = open("aFile.txt", "r")

if fileobj:
    print("Opened successfully")

# content = fileobj.read(15)    #length specifications
# print(content)

# content = fileobj.read()      #reads entire file
# print(content)

for i in fileobj:  # reads line wise
    print(i)

# print(type(content))

fileobj.close()
