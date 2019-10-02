with open("bFile.txt","ab+") as fileobj:
    print(fileobj.tell())
    print(fileobj.readline())
    print(fileobj.tell())
    # print(fileobj.readline())
    # print(fileobj.tell())

    fileobj.seek(-5,2)
    print(fileobj.readline())